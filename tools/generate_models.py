import struct
import json
import math
import os

class GLBBuilder:
    def __init__(self):
        self.bin_data = bytearray()
        self.accessors = []
        self.buffer_views = []
        self.meshes = []
        self.nodes = []
        self.materials = []
        self.scenes = [{"nodes": []}]
        self.scene = 0

    def add_material(self, name, base_color=(1, 1, 1, 1), emissive=(0, 0, 0), metallic=0.1, roughness=0.7):
        mat = {
            "name": name,
            "pbrMetallicRoughness": {
                "baseColorFactor": list(base_color),
                "metallicFactor": metallic,
                "roughnessFactor": roughness
            },
            "emissiveFactor": list(emissive),
            "doubleSided": True
        }
        self.materials.append(mat)
        return len(self.materials) - 1

    def _pad_bin(self, alignment=4):
        pad = (alignment - (len(self.bin_data) % alignment)) % alignment
        if pad > 0:
            self.bin_data.extend(b'\x00' * pad)

    def _add_buffer_view(self, byte_offset, byte_length, target=None):
        bv = {
            "buffer": 0,
            "byteOffset": byte_offset,
            "byteLength": byte_length
        }
        if target:
            bv["target"] = target
        self.buffer_views.append(bv)
        return len(self.buffer_views) - 1

    def _add_accessor(self, buffer_view_idx, component_type, count, acc_type, min_val=None, max_val=None):
        acc = {
            "bufferView": buffer_view_idx,
            "byteOffset": 0,
            "componentType": component_type,
            "count": count,
            "type": acc_type
        }
        if min_val is not None:
            acc["min"] = min_val
        if max_val is not None:
            acc["max"] = max_val
        self.accessors.append(acc)
        return len(self.accessors) - 1

    def add_mesh_primitive(self, positions, normals, indices, material_idx=0):
        # Positions: float32, VEC3
        self._pad_bin(4)
        pos_offset = len(self.bin_data)
        min_p = [min(p[i] for p in positions) for i in range(3)]
        max_p = [max(p[i] for p in positions) for i in range(3)]
        for p in positions:
            self.bin_data.extend(struct.pack('<fff', p[0], p[1], p[2]))
        pos_len = len(self.bin_data) - pos_offset
        pos_bv = self._add_buffer_view(pos_offset, pos_len, 34962) # ARRAY_BUFFER
        pos_acc = self._add_accessor(pos_bv, 5126, len(positions), "VEC3", min_p, max_p)

        # Normals: float32, VEC3
        self._pad_bin(4)
        norm_offset = len(self.bin_data)
        for n in normals:
            self.bin_data.extend(struct.pack('<fff', n[0], n[1], n[2]))
        norm_len = len(self.bin_data) - norm_offset
        norm_bv = self._add_buffer_view(norm_offset, norm_len, 34962)
        norm_acc = self._add_accessor(norm_bv, 5126, len(normals), "VEC3")

        # Indices: uint16, SCALAR
        self._pad_bin(4)
        idx_offset = len(self.bin_data)
        for idx in indices:
            self.bin_data.extend(struct.pack('<H', idx))
        idx_len = len(self.bin_data) - idx_offset
        idx_bv = self._add_buffer_view(idx_offset, idx_len, 34963) # ELEMENT_ARRAY_BUFFER
        idx_acc = self._add_accessor(idx_bv, 5123, len(indices), "SCALAR", [min(indices)], [max(indices)])

        mesh_idx = len(self.meshes)
        self.meshes.append({
            "primitives": [{
                "attributes": {
                    "POSITION": pos_acc,
                    "NORMAL": norm_acc
                },
                "indices": idx_acc,
                "material": material_idx
            }]
        })

        node_idx = len(self.nodes)
        self.nodes.append({"mesh": mesh_idx})
        self.scenes[0]["nodes"].append(node_idx)

    def write_glb(self, filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        # Pad binary buffer
        self._pad_bin(4)
        bin_length = len(self.bin_data)

        gltf_json = {
            "asset": {"version": "2.0", "generator": "LumenDriftAssetGen"},
            "scene": 0,
            "scenes": self.scenes,
            "nodes": self.nodes,
            "meshes": self.meshes,
            "materials": self.materials,
            "accessors": self.accessors,
            "bufferViews": self.buffer_views,
            "buffers": [{"byteLength": bin_length}]
        }

        json_bytes = json.dumps(gltf_json, separators=(',', ':')).encode('utf-8')
        json_pad = (4 - (len(json_bytes) % 4)) % 4
        if json_pad > 0:
            json_bytes += b' ' * json_pad

        json_chunk_len = len(json_bytes)
        bin_chunk_len = bin_length

        total_file_len = 12 + 8 + json_chunk_len + (8 + bin_chunk_len if bin_chunk_len > 0 else 0)

        with open(filepath, 'wb') as f:
            # 12-byte Header
            f.write(struct.pack('<III', 0x46546C67, 2, total_file_len))
            # Chunk 0: JSON
            f.write(struct.pack('<II', json_chunk_len, 0x4E4F534A))
            f.write(json_bytes)
            # Chunk 1: BIN
            if bin_chunk_len > 0:
                f.write(struct.pack('<II', bin_chunk_len, 0x004E4942))
                f.write(self.bin_data)

        print(f"Generated GLB: {filepath} ({total_file_len} bytes)")

def create_creature_head(filepath):
    glb = GLBBuilder()
    # Emissive glowing cyan body
    mat_cyan = glb.add_material("CreatureGlowCyan", base_color=(0.1, 0.9, 1.0, 1.0), emissive=(0.0, 0.9, 1.0), metallic=0.2, roughness=0.3)
    
    # Generate streamlined teardrop/tadpole head mesh (UV sphere deformed)
    positions = []
    normals = []
    indices = []
    
    stacks = 16
    slices = 20
    
    for i in range(stacks + 1):
        v = i / stacks
        phi = v * math.pi
        sin_phi = math.sin(phi)
        cos_phi = math.cos(phi)
        
        for j in range(slices + 1):
            u = j / slices
            theta = u * 2.0 * math.pi
            sin_theta = math.sin(theta)
            cos_theta = math.cos(theta)
            
            # Base sphere
            nx = sin_phi * cos_theta
            ny = cos_phi
            nz = sin_phi * sin_theta
            
            # Deform into hydrodynamic tadpole head:
            # Stretched forward along Z, slightly flattened Y, tapered back
            z_pos = (nz - 0.2) * 1.2
            x_pos = nx * 0.7 * (1.0 - 0.3 * nz)
            y_pos = ny * 0.55 * (1.0 - 0.3 * nz)
            
            positions.append((x_pos, y_pos, z_pos))
            # Normal approximation
            l = math.sqrt(x_pos*x_pos + y_pos*y_pos + z_pos*z_pos) or 1.0
            normals.append((x_pos/l, y_pos/l, z_pos/l))
            
    for i in range(stacks):
        for j in range(slices):
            p1 = i * (slices + 1) + j
            p2 = p1 + (slices + 1)
            indices.extend([p1, p2, p1 + 1])
            indices.extend([p1 + 1, p2, p2 + 1])
            
    glb.add_mesh_primitive(positions, normals, indices, mat_cyan)
    glb.write_glb(filepath)

def create_creature_tail_segment(filepath):
    glb = GLBBuilder()
    mat_tail = glb.add_material("TailCyanEmissive", base_color=(0.05, 0.8, 0.95, 1.0), emissive=(0.0, 0.7, 0.9), metallic=0.1, roughness=0.4)
    
    positions = []
    normals = []
    indices = []
    
    stacks = 8
    slices = 12
    for i in range(stacks + 1):
        phi = (i / stacks) * math.pi
        sin_phi = math.sin(phi)
        cos_phi = math.cos(phi)
        for j in range(slices + 1):
            theta = (j / slices) * 2.0 * math.pi
            nx = sin_phi * math.cos(theta)
            ny = cos_phi
            nz = sin_phi * math.sin(theta)
            
            # Tapered organic bead
            x = nx * 0.35
            y = ny * 0.3
            z = nz * 0.45
            positions.append((x, y, z))
            l = math.sqrt(x*x + y*y + z*z) or 1.0
            normals.append((x/l, y/l, z/l))
            
    for i in range(stacks):
        for j in range(slices):
            p1 = i * (slices + 1) + j
            p2 = p1 + (slices + 1)
            indices.extend([p1, p2, p1 + 1])
            indices.extend([p1 + 1, p2, p2 + 1])
            
    glb.add_mesh_primitive(positions, normals, indices, mat_tail)
    glb.write_glb(filepath)

def create_collectible_node(filepath):
    glb = GLBBuilder()
    # Bright energetic turquoise / cyan crystal core
    mat_node = glb.add_material("CollectibleNodeMat", base_color=(0.2, 1.0, 0.9, 1.0), emissive=(0.0, 1.0, 0.8), metallic=0.8, roughness=0.1)
    
    # Regular Icosahedron (12 vertices, 20 triangular faces)
    t = (1.0 + math.sqrt(5.0)) / 2.0
    scale = 0.45
    raw_verts = [
        (-1, t, 0), (1, t, 0), (-1, -t, 0), (1, -t, 0),
        (0, -1, t), (0, 1, t), (0, -1, -t), (0, 1, -t),
        (t, 0, -1), (t, 0, 1), (-t, 0, -1), (-t, 0, 1)
    ]
    # Normalize and scale
    positions = []
    normals = []
    for (x, y, z) in raw_verts:
        l = math.sqrt(x*x + y*y + z*z)
        nx, ny, nz = x/l, y/l, z/l
        positions.append((nx * scale, ny * scale, nz * scale))
        normals.append((nx, ny, nz))
        
    faces = [
        (0, 11, 5), (0, 5, 1), (0, 1, 7), (0, 7, 10), (0, 10, 11),
        (1, 5, 9), (5, 11, 4), (11, 10, 2), (10, 7, 6), (7, 1, 8),
        (3, 9, 4), (3, 4, 2), (3, 2, 6), (3, 6, 8), (3, 8, 9),
        (4, 9, 5), (2, 4, 11), (6, 2, 10), (8, 6, 7), (9, 8, 1)
    ]
    indices = []
    for f in faces:
        indices.extend(f)
        
    glb.add_mesh_primitive(positions, normals, indices, mat_node)
    glb.write_glb(filepath)

def create_hazard_tendril(filepath):
    glb = GLBBuilder()
    # Dangerous bioluminescent magenta/violet spikes
    mat_magenta = glb.add_material("TendrilHazardMat", base_color=(1.0, 0.0, 0.5, 1.0), emissive=(1.0, 0.05, 0.45), metallic=0.3, roughness=0.3)
    
    # 4 curved spiky horns branching from a base
    positions = []
    normals = []
    indices = []
    
    def add_cone(tip, base_center, radius, segments=8):
        base_start = len(positions)
        # Base ring
        for s in range(segments):
            angle = (s / segments) * 2.0 * math.pi
            bx = base_center[0] + radius * math.cos(angle)
            by = base_center[1]
            bz = base_center[2] + radius * math.sin(angle)
            positions.append((bx, by, bz))
            normals.append((math.cos(angle), -0.2, math.sin(angle)))
        
        # Tip vertex
        tip_idx = len(positions)
        positions.append(tip)
        normals.append((0, 1, 0))
        
        # Triangles
        for s in range(segments):
            next_s = (s + 1) % segments
            indices.extend([base_start + s, base_start + next_s, tip_idx])
            
    # Central tall spike
    add_cone((0.0, 1.8, 0.0), (0.0, 0.0, 0.0), 0.35)
    # Side branches curved outwards
    add_cone((0.7, 1.3, 0.3), (0.1, 0.0, 0.1), 0.22)
    add_cone((-0.6, 1.2, -0.2), (-0.1, 0.0, -0.1), 0.22)
    add_cone((0.2, 1.0, -0.6), (0.0, 0.0, -0.1), 0.18)
    
    glb.add_mesh_primitive(positions, normals, indices, mat_magenta)
    glb.write_glb(filepath)

def create_obstacle_pillar(filepath):
    glb = GLBBuilder()
    # Dark organic biological wall with subtle violet emissive edges
    mat_obs = glb.add_material("ObstaclePillarMat", base_color=(0.04, 0.05, 0.12, 1.0), emissive=(0.3, 0.0, 0.4), metallic=0.2, roughness=0.8)
    
    # An irregular organic column (cylinder with perturbed vertices)
    positions = []
    normals = []
    indices = []
    
    rings = 10
    slices = 12
    height = 5.0
    
    for r in range(rings + 1):
        v = r / rings
        y = (v - 0.5) * height
        radius = 0.9 + 0.35 * math.sin(v * math.pi * 3.0) # Organic bulging
        for s in range(slices + 1):
            theta = (s / slices) * 2.0 * math.pi
            # Subtle perturbation
            r_pert = radius * (1.0 + 0.15 * math.sin(theta * 3.0 + v * 2.0))
            x = r_pert * math.cos(theta)
            z = r_pert * math.sin(theta)
            positions.append((x, y, z))
            l = math.sqrt(x*x + z*z) or 1.0
            normals.append((x/l, 0.1 * math.sin(v * math.pi), z/l))
            
    for r in range(rings):
        for s in range(slices):
            p1 = r * (slices + 1) + s
            p2 = p1 + (slices + 1)
            indices.extend([p1, p2, p1 + 1])
            indices.extend([p1 + 1, p2, p2 + 1])
            
    glb.add_mesh_primitive(positions, normals, indices, mat_obs)
    glb.write_glb(filepath)

def create_tunnel_segment(filepath, is_curved=False):
    glb = GLBBuilder()
    mat_wall = glb.add_material("TunnelWallMat", base_color=(0.02, 0.03, 0.08, 1.0), emissive=(0.0, 0.08, 0.15), metallic=0.1, roughness=0.9)
    
    positions = []
    normals = []
    indices = []
    
    rings = 16
    slices = 20
    length = 16.0
    tunnel_radius = 4.2
    
    for r in range(rings + 1):
        t = r / rings
        if is_curved:
            # Curve 30 degrees (0.52 rad) along X
            curve_angle = t * 0.52
            center_x = 15.0 * (1.0 - math.cos(curve_angle))
            center_z = 15.0 * math.sin(curve_angle)
            tangent_angle = curve_angle
        else:
            center_x = 0.0
            center_z = t * length
            tangent_angle = 0.0
            
        cos_tangent = math.cos(tangent_angle)
        sin_tangent = math.sin(tangent_angle)
        
        # Ribbed organic effect
        rad = tunnel_radius * (1.0 + 0.05 * math.cos(t * math.pi * 8.0))
        
        for s in range(slices + 1):
            theta = (s / slices) * 2.0 * math.pi
            rx = rad * math.cos(theta)
            ry = rad * math.sin(theta)
            
            # Rotate along tunnel tangent
            world_x = center_x + rx * cos_tangent
            world_y = ry
            world_z = center_z + rx * (-sin_tangent)
            
            positions.append((world_x, world_y, world_z))
            # Normal facing INWARDS for the interior tunnel
            normals.append((-math.cos(theta) * cos_tangent, -math.sin(theta), math.cos(theta) * sin_tangent))
            
    for r in range(rings):
        for s in range(slices):
            p1 = r * (slices + 1) + s
            p2 = p1 + (slices + 1)
            # Inward facing winding order
            indices.extend([p1, p1 + 1, p2])
            indices.extend([p1 + 1, p2 + 1, p2])
            
    glb.add_mesh_primitive(positions, normals, indices, mat_wall)
    glb.write_glb(filepath)

if __name__ == '__main__':
    create_creature_head('assets/models/creature_head.glb')
    create_creature_tail_segment('assets/models/creature_tail_segment.glb')
    create_collectible_node('assets/models/collectible_node.glb')
    create_hazard_tendril('assets/models/hazard_tendril.glb')
    create_obstacle_pillar('assets/models/obstacle_pillar.glb')
    create_tunnel_segment('assets/models/tunnel_segment_straight.glb', is_curved=False)
    create_tunnel_segment('assets/models/tunnel_segment_curved.glb', is_curved=True)
    print("All 3D models created successfully!")

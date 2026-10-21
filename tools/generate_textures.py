from PIL import Image, ImageDraw
import math
import os

def create_particle_glow(filepath):
    size = 256
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    center = size / 2.0
    radius = size / 2.0
    
    pixels = img.load()
    for y in range(size):
        for x in range(size):
            dx = x - center
            dy = y - center
            dist = math.sqrt(dx * dx + dy * dy)
            if dist < radius:
                # Radial exponential fade
                norm = dist / radius
                alpha = int(255 * max(0.0, (1.0 - norm) ** 2.2))
                # Cyan glow
                r = int(0 * norm + 0 * (1 - norm))
                g = int(200 + 55 * (1 - norm))
                b = 255
                pixels[x, y] = (r, g, b, alpha)
                
    img.save(filepath, "PNG")
    print(f"Generated {filepath}")

def create_timer_icon(filepath):
    size = 256
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer ring (cyan glow)
    draw.ellipse([30, 45, 226, 241], outline=(0, 229, 255, 240), width=12)
    # Inner stopwatch knob / top button
    draw.rectangle([116, 12, 140, 45], fill=(0, 229, 255, 255))
    draw.rectangle([100, 10, 156, 20], fill=(0, 229, 255, 255))
    # Clock hands
    draw.line([128, 143, 128, 75], fill=(0, 255, 230, 255), width=8)
    draw.line([128, 143, 175, 143], fill=(255, 0, 127, 255), width=8)
    draw.ellipse([120, 135, 136, 151], fill=(255, 255, 255, 255))
    
    img.save(filepath, "PNG")
    print(f"Generated {filepath}")

def create_emissive_wall_map(diffuse_path, emissive_path):
    if not os.path.exists(diffuse_path):
        return
    img = Image.open(diffuse_path).convert("RGB")
    emissive = Image.new("RGB", img.size)
    
    src_px = img.load()
    dst_px = emissive.load()
    w, h = img.size
    
    for y in range(h):
        for x in range(w):
            r, g, b = src_px[x, y]
            # Isolate vibrant cyan (high b & g, lower r) and magenta (high r & b, lower g)
            brightness = (r + g + b) / 3.0
            if (b > 120 and g > 110 and r < 140) or (r > 120 and b > 110 and g < 100):
                # Glowing vein
                dst_px[x, y] = (min(255, int(r * 1.5)), min(255, int(g * 1.5)), min(255, int(b * 1.5)))
            else:
                dst_px[x, y] = (int(r * 0.1), int(g * 0.1), int(b * 0.1))
                
    emissive.save(emissive_path, "PNG")
    print(f"Generated {emissive_path}")

if __name__ == "__main__":
    create_particle_glow("assets/textures/particle_glow.png")
    create_timer_icon("assets/textures/ui/icon_timer.png")
    create_emissive_wall_map("assets/textures/organic_wall_diffuse.jpg", "assets/textures/organic_wall_emissive.png")

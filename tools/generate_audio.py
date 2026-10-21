import wave
import math
import struct
import os
import random

SAMPLE_RATE = 44100

def create_wave_file(filename, samples):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(SAMPLE_RATE)
        packed_frames = bytearray()
        for s in samples:
            # Clamp to [-1.0, 1.0]
            s = max(-1.0, min(1.0, s))
            int_sample = int(s * 32767.0)
            packed_frames.extend(struct.pack('<h', int_sample))
        wf.writeframes(packed_frames)
    print(f"Generated {filename} ({len(samples)} samples, {len(samples)/SAMPLE_RATE:.2f}s)")

def generate_ambient_underwater(filepath):
    # 6.0 second seamless loopable deep ambient hum with oceanic current fluctuation
    duration = 6.0
    num_samples = int(SAMPLE_RATE * duration)
    samples = []
    random.seed(42)
    
    # Pre-generate smooth noise
    noise_buffer = [random.uniform(-1, 1) for _ in range(num_samples)]
    # Simple lowpass moving average
    filtered_noise = [0.0] * num_samples
    val = 0.0
    alpha = 0.02
    for i in range(num_samples):
        val += alpha * (noise_buffer[i] - val)
        filtered_noise[i] = val

    for i in range(num_samples):
        t = i / SAMPLE_RATE
        # Seamless loop phase
        phase_loop = 2.0 * math.pi * (i / num_samples)
        
        # Deep drone chords: 55Hz (A1), 82.4Hz (E2), 110Hz (A2)
        base_drone = 0.35 * math.sin(2.0 * math.pi * 55.0 * t)
        sub_fifth = 0.20 * math.sin(2.0 * math.pi * 82.4 * t)
        octave = 0.15 * math.sin(2.0 * math.pi * 110.0 * t + 0.5)
        
        # Slow pulsating fluid modulation (LFO)
        lfo = 0.5 + 0.5 * math.sin(phase_loop * 3.0)
        fluid_layer = 0.18 * filtered_noise[i] * (0.8 + 0.4 * lfo)
        
        # Shimmer harmonic
        shimmer = 0.05 * math.sin(2.0 * math.pi * 220.0 * t + math.sin(phase_loop * 2))
        
        sample = (base_drone + sub_fifth + octave + fluid_layer + shimmer) * 0.7
        samples.append(sample)
        
    create_wave_file(filepath, samples)

def generate_collect_node(filepath):
    # 0.6s crystalline / bioluminescent harmonic chime
    duration = 0.6
    num_samples = int(SAMPLE_RATE * duration)
    samples = []
    
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        # Envelope: crisp instant attack (5ms), smooth exponential decay
        if t < 0.005:
            env = t / 0.005
        else:
            env = math.exp(-(t - 0.005) * 6.5)
        
        # Multi-harmonic crystalline frequency: 880Hz (A5), 1320Hz (E6), 1760Hz (A6), 2640Hz (E7)
        c1 = 0.40 * math.sin(2.0 * math.pi * 880.0 * t)
        c2 = 0.30 * math.sin(2.0 * math.pi * 1320.0 * t)
        c3 = 0.20 * math.sin(2.0 * math.pi * 1760.0 * t)
        c4 = 0.10 * math.sin(2.0 * math.pi * 2640.0 * t)
        
        sample = (c1 + c2 + c3 + c4) * env * 0.85
        samples.append(sample)
        
    create_wave_file(filepath, samples)

def generate_collision_crash(filepath):
    # 0.8s deep organic impact with low sub sweep and dissipating crackle
    duration = 0.8
    num_samples = int(SAMPLE_RATE * duration)
    samples = []
    random.seed(123)
    
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        # Impact envelope: sharp attack, decay
        if t < 0.003:
            env = t / 0.003
        else:
            env = math.exp(-(t - 0.003) * 5.0)
            
        # Pitch downward drop: 160Hz dropping down to 40Hz
        freq = 40.0 + 120.0 * math.exp(-t * 15.0)
        sub_impact = 0.55 * math.sin(2.0 * math.pi * freq * t)
        
        # Burst noise
        noise = (random.random() * 2.0 - 1.0) * math.exp(-t * 22.0) * 0.35
        # Secondary rumble
        rumble = 0.25 * math.sin(2.0 * math.pi * 45.0 * t) * math.exp(-t * 3.5)
        
        sample = (sub_impact + noise + rumble) * env * 0.9
        samples.append(sample)
        
    create_wave_file(filepath, samples)

def generate_whoosh_boost(filepath):
    # 0.5s fluid velocity whoosh
    duration = 0.5
    num_samples = int(SAMPLE_RATE * duration)
    samples = []
    random.seed(999)
    
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        # Bell curve envelope
        env = math.sin(math.pi * (i / num_samples)) ** 2
        # Swept frequency modulation
        carrier = math.sin(2.0 * math.pi * (140.0 + 220.0 * (t / duration)) * t)
        noise = (random.random() * 2.0 - 1.0) * 0.4
        
        sample = (carrier * 0.4 + noise * 0.6) * env * 0.75
        samples.append(sample)
        
    create_wave_file(filepath, samples)

if __name__ == '__main__':
    generate_ambient_underwater('assets/audio/ambient_underwater.wav')
    generate_collect_node('assets/audio/collect_node.wav')
    generate_collision_crash('assets/audio/collision_crash.wav')
    generate_whoosh_boost('assets/audio/whoosh_boost.wav')
    print("All audio assets created successfully!")

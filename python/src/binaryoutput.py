from pathlib import Path

def generate_deterministic_binary(filename, seed=42, size=1024, pattern_size=128):
    pattern = bytearray()
    rng = lambda: (seed + len(pattern)) % 256  # Simple deterministic PRNG
    
    # Generate unique pattern based on seed
    while len(pattern) < pattern_size:
        pattern.append(rng())
        pattern.append(rng() ^ 0xEF)  # Add some variation with bitwise ops
    
    # Write repeating pattern to file
    with Path(filename).open('wb') as f:
        for _ in range(size // pattern_size):
            f.write(pattern)
        f.write(pattern[:size % pattern_size])  # Remainder

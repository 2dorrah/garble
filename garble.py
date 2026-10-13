#!/usr/bin/env python3
"""
CYTHANX_GARBLE.py
A symbolic / fictional "thought-garble" interpreter based on the
Human × Plant diagram.

This is a computational metaphor, not a model of literal biological
transcription or human cognition.
"""

from dataclasses import dataclass
import hashlib

# --- CYTHANX symbolic vocabulary --------------------------------------------

TOKENS = {
    "001": "PLANT",
    "010": "BLOOD",
    "011": "CELL",
    "100": "SIGNAL",
    "101": "NEURAL",
    "110": "AUTONOMIC",
    "111": "MOTOR",
    "000": "COGNITION",
}

GARBLE = {
    "PLANT": "KRA",
    "BLOOD": "BLO",
    "CELL": "NEX",
    "SIGNAL": "SIG",
    "NEURAL": "NEU",
    "AUTONOMIC": "SOL",
    "MOTOR": "MOR",
    "COGNITION": "CYR",
    "ENVIRONMENT": "EKO",
}

# Initial symbolic stream reconstructed from the diagram's flow.
SEED = "001010011100101110111000"

@dataclass
class State:
    bits: str
    cycle: int = 0

def garble(bits: str, cycle: int) -> str:
    """Create deterministic symbolic noise from the current state."""
    digest = hashlib.sha256(f"{bits}:{cycle}".encode()).digest()
    mask = "".join(f"{b:08b}" for b in digest)[:len(bits)]

    # XOR + circular rotation: deliberately fictional state transformation.
    mixed = "".join("1" if a != b else "0" for a, b in zip(bits, mask))
    shift = (cycle + int(bits[:3], 2)) % len(mixed)
    return mixed[shift:] + mixed[:shift]

def decode(bits: str):
    """Decode 3-bit symbols into CYTHANX concepts."""
    usable = len(bits) - (len(bits) % 3)
    return [TOKENS[bits[i:i+3]] for i in range(0, usable, 3)]

def scriptify(states):
    """Translate concepts into the fictional CYTHANX script."""
    out = []
    for word in states:
        out.append(GARBLE.get(word, word))
    return "-".join(out)

def run(seed=SEED, cycles=5):
    state = State(seed)

    print("=== CYTHANX THOUGHT-GARBLE ===")
    print("seed:", state.bits)
    print()

    for _ in range(cycles):
        concepts = decode(state.bits)
        glyphs = scriptify(concepts)

        print(f"[{state.cycle:02d}]")
        print(" binary :", state.bits)
        print(" states :", " -> ".join(concepts))
        print(" garble :", glyphs)

        # Environmental feedback closes the symbolic loop.
        feedback = "EKO"
        print(" feedback:", feedback)
        print()

        state.bits = garble(state.bits, state.cycle)
        state.cycle += 1

if __name__ == "__main__":
    run()

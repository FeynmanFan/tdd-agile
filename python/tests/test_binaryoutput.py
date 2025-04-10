import pytest
import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.binaryoutput import generate_deterministic_binary

def test_generate_binary_output():
    filename = Path(Path.cwd() / "binary.bin")
    generate_deterministic_binary(filename, 42)

    reference_path = Path(Path.cwd() / "tests/reference_binary.bin")

    assert Path(reference_path).read_bytes() == Path(filename).read_bytes()
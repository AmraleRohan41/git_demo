"""Sample module for Pylint testing."""

import sys  # Remove this line

def calculate(a, b, c):  # Fix spacing, drop extra arg
    """Calculates a * c after adding a + b."""
    x = a + b
    print(x * c)
    return x

def main():
    calculate(1, 2, 3)  # Match args
    # Shorten long lines, etc.

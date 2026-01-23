"""Sample module demonstrating Pylint best practices."""

def calculate(a, b, c):
    """Calculate sum of a+b multiplied by c.
    
    Args:
        a (int): First number
        b (int): Second number  
        c (int): Multiplier
        
    Returns:
        int: Result of (a + b) * c
    """
    result = a + b
    print(result * c)
    return result

def main():
    """Main entry point."""
    calculate(1, 2, 3)

if __name__ == "__main__":
    main()

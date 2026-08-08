def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract the second integer from the first."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


def divide(a: int, b: int) -> float:
    """
    Divide the first integer by the second.

    Raises
    ------
    ValueError
        If the divisor is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b

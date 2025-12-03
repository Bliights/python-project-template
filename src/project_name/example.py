def add(a: int, b: int) -> None:
    return a + b


def subtract(a: int, b: int) -> None:
    return a - b


def multiply(a: int, b: int) -> None:
    return a * b


def divide(a: int, b: int) -> None:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

import pytest

from project_name.example import add, multiply, subtract


def test_add(numbers: list[int]) -> None:
    assert add(numbers[0], numbers[1]) == 0


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 2, 1),
        (2, 3, -1),
        (0, 0, 0),
    ],
)
def test_subtract(a: int, b: int, expected: int) -> None:
    assert subtract(a, b) == expected


def test_multiply() -> None:
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

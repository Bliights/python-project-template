import pytest

from project_name.example import divide


def test_divide(integer_triplet: tuple[int, int, float]) -> None:
    a, b, expected = integer_triplet
    assert divide(a, b) == expected


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(5, 0)

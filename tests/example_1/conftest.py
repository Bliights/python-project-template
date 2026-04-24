import pytest


@pytest.fixture
def numbers() -> list[int]:
    """Simple fixture"""
    return [1, -1, 0, 3, -3]

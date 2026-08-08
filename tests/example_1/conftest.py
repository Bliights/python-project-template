import pytest


@pytest.fixture
def numbers() -> list[int]:
    """Return a simple fixture."""
    return [1, -1, 0, 3, -3]

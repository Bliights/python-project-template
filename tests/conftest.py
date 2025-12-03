import pytest


@pytest.fixture
def numbers() -> list[int]:
    """Simple fixture"""
    return [1, -1, 0, 3, -3]


@pytest.fixture(
    params=[
        (6, 3, 2),
        (6, -3, -2),
        (-6, -3, 2),
    ],
)
def integer_triplet(request: pytest.FixtureRequest) -> tuple[int, int]:
    """Parameterized fixture."""
    return request.param

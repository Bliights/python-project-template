import pytest


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

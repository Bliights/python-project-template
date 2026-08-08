import logging

from project_name.example import add
from scripts.utils.logging_config import disable_logging, setup_logging

logger = logging.getLogger(__name__)
setup_logging(logging.DEBUG)


@disable_logging(logging.INFO)
def test() -> None:
    """Test the disable logging decorator."""
    logger.info("test")


if __name__ == "__main__":
    logger.info(add(1, 1))
    test()

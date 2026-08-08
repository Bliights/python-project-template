import structlog

from project_name.example import add, divide
from scripts.utils.logging_config import LogLevel, disable_logging, setup_logging

setup_logging(LogLevel.DEBUG)
logger = structlog.get_logger(__name__)


@disable_logging(LogLevel.INFO)
def test() -> None:
    """Test the disable logging decorator."""
    logger.info("test_disable")


if __name__ == "__main__":
    logger.info("test_addition", value=add(1, 1))
    test()
    try:
        divide(10, 0)
    except ZeroDivisionError:
        logger.exception(
            "division_failed",
            numerator=10,
            denominator=0,
        )

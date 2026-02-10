import logging

from project_name.example import add

from .logging_config import setup_logging

logger = logging.getLogger(__name__)
setup_logging(logging.DEBUG)


if __name__ == "__main__":
    logger.info(add(1, 1))

import logging

LOG_FORMAT = "[%(levelname)s] : %(message)s"


class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: "\033[92m",  # Green
        logging.INFO: "\033[96m",  # Cyan
        logging.WARNING: "\033[93m",  # Yellow
        logging.ERROR: "\033[91m",  # Red
        logging.CRITICAL: "\033[91;1m",  # Bold red
    }
    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record by applying a color based on its severity level

        Parameters
        ----------
        record : logging.LogRecord
            The log record containing all information about the logging event

        Returns
        -------
        str
            The formatted log message with the color codes applied
        """
        color = self.COLORS.get(record.levelno, self.RESET)
        message = super().format(record)
        return f"{color}{message}{self.RESET}"


def setup_logging(level: int = logging.INFO) -> None:
    """
    Configure the root logger for the entire application

    Parameters
    ----------
    level : str, optional
        Minimum logging level to display
    """
    handler = logging.StreamHandler()
    handler.setFormatter(ColorFormatter(LOG_FORMAT))

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers.clear()
    root_logger.addHandler(handler)

from __future__ import annotations

import logging
import os
import sys
from enum import IntEnum, StrEnum
from functools import wraps
from typing import TYPE_CHECKING, ParamSpec, TypeVar

import structlog

if TYPE_CHECKING:
    from collections.abc import Callable

P = ParamSpec("P")
R = TypeVar("R")


class LogFormat(StrEnum):
    """Available log output formats."""

    JSON = "json"
    CONSOLE = "console"


class LogLevel(IntEnum):
    """Available logging levels."""

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


LIBRARY_LOG_LEVELS: dict[str, LogLevel] = {
    "httpx": LogLevel.WARNING,
    "urllib3": LogLevel.WARNING,
}


def setup_logging(level: LogLevel = LogLevel.INFO) -> None:
    """
    Configure structured logging for the entire application.

    Logs are emitted as JSON by default, suitable for observability tools.
    Set ``LOG_FORMAT=console`` to enable human-readable Rich logs.

    Parameters
    ----------
    level : LogLevel, optional
        Minimum logging level to emit.
    """
    log_format = LogFormat(os.getenv("LOG_FORMAT", LogFormat.JSON).lower())
    console_mode = log_format is LogFormat.CONSOLE

    shared_processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
    ]

    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            *shared_processors,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    if console_mode:
        renderer = structlog.dev.ConsoleRenderer(
            force_colors=True,
            exception_formatter=structlog.dev.RichTracebackFormatter(
                show_locals=False,
            ),
        )
        renderer_processors = []
    else:
        renderer = structlog.processors.JSONRenderer()
        renderer_processors = [
            structlog.processors.dict_tracebacks,
        ]

    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=[
            *shared_processors,
            structlog.stdlib.ExtraAdder(),
        ],
        processors=[
            structlog.processors.UnicodeDecoder(),
            *renderer_processors,
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            renderer,
        ],
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.addHandler(handler)
    root_logger.setLevel(level)

    for logger_name, logger_level in LIBRARY_LOG_LEVELS.items():
        logging.getLogger(logger_name).setLevel(logger_level)


def disable_logging(
    level: LogLevel = LogLevel.INFO,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Temporarily disable logging during execution of a decorated function.

    Parameters
    ----------
    level : LogLevel, optional
        Logging level to disable.

    Returns
    -------
    Callable[[Callable[P, R]], Callable[P, R]]
        Decorator that ignores log messages at or below the specified level while preserving the decorated
        function's signature.
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            previous_level = logging.root.manager.disable
            logging.disable(level)
            try:
                return func(*args, **kwargs)
            finally:
                logging.disable(previous_level)

        return wrapper

    return decorator

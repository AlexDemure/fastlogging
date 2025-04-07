import logging
from typing import Any, Callable, Dict, List, Optional, Tuple

from gadlogger import const, mappers
from gadlogger.utils import fields


class Formatter(logging.Formatter):
    def __init__(
        self,
        message: Optional[List[Tuple[str, Callable[[logging.LogRecord], Any]]]] = None,
        hidden: Optional[List[str]] = None,
        context: Optional[Callable[[], Dict]] = None,
    ) -> None:
        super().__init__()
        self.message = message if message else mappers.LOGGING_MESSAGE_FIELDS
        self.hidden = hidden if hidden else []
        self.context = context if context else lambda: {}

    def enrich(self, record: logging.LogRecord) -> None:
        for field, func in self.message:
            setattr(record, field, func(record))

        if self.context:
            for key, value in self.context().items():
                setattr(record, key, value)

        if record.levelno >= logging.WARNING and record.exc_info:
            setattr(record, "stacktrace", self.formatException(record.exc_info))
            setattr(record, "exception", str(record.exc_info[1]))

        if self.hidden:
            for key, value in record.__dict__.items():
                if key not in const.LOGGING_RESERVED_FIELDS:
                    setattr(record, key, fields.parsehidden(value, self.hidden))

        for key, value in record.__dict__.items():
            if key not in const.LOGGING_RESERVED_FIELDS:
                setattr(record, key, fields.parsenone(value))

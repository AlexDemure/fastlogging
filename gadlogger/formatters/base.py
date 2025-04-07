import logging
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from gadlogger import const
from gadlogger import mappers
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

    def getcontext(self, record: logging.LogRecord) -> None:
        context = {}

        for field, func in self.message:
            setattr(record, field, fields.to_empty(func(record)))

        data = record.__dict__

        if self.context:
            data.update(self.context())

        for key, value in data.items():
            if not (key in const.LOGGING_RESERVED_FIELDS or key in self.message):
                context[key] = fields.to_empty(value)

        if context:
            setattr(record, "context", context)

        if record.levelno >= logging.WARNING and record.exc_info:
            setattr(record, "stacktrace", self.formatException(record.exc_info))

        if self.hidden:
            for key, value in record.__dict__.items():
                setattr(record, key, fields.to_sensitive(value, self.hidden))

import logging
import typing

from gadlogger import const
from gadlogger import mappers
from gadlogger.utils import fields


class Formatter(logging.Formatter):
    def __init__(
        self,
        message: typing.Optional[
            typing.List[typing.Tuple[str, typing.Callable[[logging.LogRecord], typing.Any]]]
        ] = None,
        hidden: typing.Optional[typing.List[str]] = None,
        context: typing.Optional[typing.Callable[[], typing.Dict]] = None,
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

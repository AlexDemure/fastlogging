import logging

from gadlogger.formatters.base import Formatter
from gadlogger.utils import fields


class PlainFormatter(Formatter):
    def format(self, record: logging.LogRecord) -> str:
        self.enrich(record)
        self._style._fmt = "{timestamp} {level} {logger} {message} {{{context}}}".format(
            timestamp=fields.to_format("timestamp"),
            level=f"[{fields.to_format('level')}]",
            logger=fields.to_format("logger"),
            message=fields.to_format("message"),
            context=", ".join(
                [
                    f"{key}: {fields.to_format(key)}"
                    for key, _ in self.message
                    if key not in {"timestamp", "level", "logger", "message"}
                ]
            ),
        )
        return super().format(record)

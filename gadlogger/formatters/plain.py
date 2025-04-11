import logging

from gadlogger.formatters.base import Formatter
from gadlogger.utils import fields


class PlainFormatter(Formatter):
    def format(self, record: logging.LogRecord) -> str:
        self.enrich(record)
        self._style._fmt = "{timestamp} {level} {logger} {message} {{{context}}}".format(
            timestamp=fields.toformat("timestamp"),
            level=f"[{fields.toformat('level')}]",
            logger=fields.toformat("logger"),
            message=fields.toformat("message"),
            context=", ".join(
                [
                    f"{key}: {fields.toformat(key)}"
                    for key, _ in self.message
                    if key not in {"timestamp", "level", "logger", "message"}
                ]
            ),
        )
        return super().format(record)

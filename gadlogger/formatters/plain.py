import logging

from gadlogger import const
from gadlogger.formatters.base import Formatter
from gadlogger.utils import fields


class PlainFormatter(Formatter):
    def format(self, record: logging.LogRecord) -> str:
        self.getcontext(record)
        self._style._fmt = const.SYMBOL_WHITESPACE.join(fields.to_format(field) for field, _ in self.message)
        return super().format(record)

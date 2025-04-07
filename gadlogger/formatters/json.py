import logging

from gadlogger.formatters.base import Formatter
from gadlogger.utils import fields


class JSONFormatter(Formatter):
    def format(self, record: logging.LogRecord) -> str:
        self.getcontext(record)
        return fields.to_json({field: getattr(record, field) for field, _ in self.message if hasattr(record, field)})

import logging

from gadify import json

from gadlogger import const
from gadlogger.formatters.base import Formatter


class JSONFormatter(Formatter):
    def format(self, record: logging.LogRecord) -> str:
        self.enrich(record)

        root = {field: getattr(record, field) for field, _ in self.message}

        context = {
            key: value
            for key, value in record.__dict__.items()
            if not key in root.keys() and key not in const.LOGGING_RESERVED_FIELDS
        }

        if context:
            root["context"] = context

        return json.tojson(root)

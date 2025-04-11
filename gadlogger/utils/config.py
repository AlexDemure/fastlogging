import logging.config
import sys

from gadify import modules

from gadlogger import formatters
from gadlogger import models


def setup(*loggers: models.Logger) -> None:
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {},
        "handlers": {},
        "loggers": {},
        "root": {},
    }

    for logger in loggers:
        formattername, formatter = "plain", formatters.PlainFormatter

        if logger.module:
            formattername = modules.define(logger.module)
            if formattername == "json":
                formatter = formatters.JSONFormatter

        if formattername not in config["formatters"]:
            config["formatters"][formattername] = {"()": formatter, **logger.kwargs}

        config["handlers"][logger.id] = {
            "class": "logging.StreamHandler",
            "stream": logger.stream or sys.stdout,
            "formatter": formattername,
        }

        if logger.name == "root":
            config["root"] = {
                "handlers": [logger.id],
                "level": logger.level,
            }
        else:
            config["loggers"][logger.name] = {
                "handlers": [logger.id],
                "level": logger.level,
                "propagate": False,
            }

    logging.config.dictConfig(config)


__all__ = ["setup"]

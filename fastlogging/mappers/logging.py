import logging
import os
from datetime import datetime
from datetime import timezone
from typing import Any
from typing import Callable
from typing import List
from typing import Tuple

LOGGING_MESSAGE_FIELDS: List[Tuple[str, Callable[[logging.LogRecord], Any]]] = [
    ("timestamp", lambda record: datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat()),
    ("level", lambda record: record.levelname),
    ("logger", lambda record: record.name),
    ("message", lambda record: record.getMessage()),
    ("trace_id", lambda record: getattr(record, "trace_id", None)),
    ("span_id", lambda record: getattr(record, "span_id", None)),
    ("user_id", lambda record: getattr(record, "user_id", None)),
    ("request_id", lambda record: getattr(record, "request_id", None)),
    ("location", lambda record: f"{record.pathname}:{record.funcName}:{record.lineno}"),
    ("elapsed", lambda record: getattr(record, "elapsed", None)),
    ("ip", lambda record: getattr(record, "ip", None)),
    ("debug", lambda record: getattr(record, "debug", None)),
    ("service", lambda record: os.getenv("SERVICE", None)),
    ("environment", lambda record: os.getenv("ENVIRONMENT", None)),
    ("version", lambda record: os.getenv("VERSION", None)),
    ("pod", lambda record: os.getenv("POD")),
    ("namespace", lambda record: os.getenv("NAMESPACE")),
    ("container", lambda record: os.getenv("CONTAINER")),
    ("process", lambda record: record.process),
    ("thread", lambda record: record.thread),
]

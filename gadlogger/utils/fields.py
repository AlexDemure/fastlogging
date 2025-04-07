import json
from typing import Any
from typing import List

from gadlogger import const


def to_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, default=str)


def to_format(value: Any) -> str:
    return f"%({value})s"


def to_empty(value: Any) -> Any:
    return const.LOGGING_NONE_VALUE if value is None else value


def to_sensitive(data: Any, hidden: List[str]) -> Any:
    if isinstance(data, dict):
        return {
            k: (const.LOGGING_HIDDEN_VALUE if k.lower() in hidden else to_sensitive(v, hidden)) for k, v in data.items()
        }
    elif isinstance(data, list):
        return [to_sensitive(i, hidden) for i in data]
    return data

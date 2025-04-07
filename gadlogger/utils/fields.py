import json
from typing import Any, List

from gadlogger import const


def to_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, default=str)


def to_format(value: Any) -> str:
    return f"%({value})s"


def parsenone(data: Any) -> Any:
    if isinstance(data, dict):
        return {k: parsenone(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [parsenone(i) for i in data]
    return const.LOGGING_NONE_VALUE if data is None else data


def parsehidden(data: Any, hidden: List[str]) -> Any:
    if isinstance(data, dict):
        return {
            k: (const.LOGGING_HIDDEN_VALUE if k.lower() in hidden else parsehidden(v, hidden)) for k, v in data.items()
        }
    elif isinstance(data, list):
        return [parsehidden(i, hidden) for i in data]
    return data

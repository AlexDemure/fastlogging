import typing

from gadlogger import const


def toformat(value: typing.Any) -> str:
    return f"%({value})s"


def parsenone(data: typing.Any) -> typing.Any:
    if isinstance(data, dict):
        return {k: parsenone(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [parsenone(i) for i in data]
    return const.LOGGING_NONE_VALUE if data is None else data


def parsehidden(data: typing.Any, hidden: typing.List[str]) -> typing.Any:
    if isinstance(data, dict):
        return {
            k: (const.LOGGING_HIDDEN_VALUE if k.lower() in hidden else parsehidden(v, hidden)) for k, v in data.items()
        }
    elif isinstance(data, list):
        return [parsehidden(i, hidden) for i in data]
    return data

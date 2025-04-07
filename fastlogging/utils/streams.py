import sys
from typing import TextIO


def getname(stream: TextIO) -> str:
    if stream is sys.stdout:
        return "stdout"
    elif stream is sys.stderr:
        return "stderr"

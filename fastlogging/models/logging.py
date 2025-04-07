import hashlib
import json
import sys
from dataclasses import dataclass
from dataclasses import field
from types import ModuleType
from typing import Dict
from typing import Optional
from typing import TextIO


@dataclass
class Logger:
    name: str
    level: int
    module: Optional[ModuleType] = None
    stream: Optional[TextIO] = sys.stdout
    kwargs: Dict = field(default_factory=dict)

    @property
    def id(self) -> str:
        return hashlib.md5(
            json.dumps(
                {
                    "name": self.name,
                    "level": self.level,
                    "stream": str(self.stream),
                    "module": str(self.module),
                    "kwargs": self.kwargs,
                },
                sort_keys=True,
                ensure_ascii=False,
            ).encode("utf-8")
        ).hexdigest()

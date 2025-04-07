from types import ModuleType
from typing import Optional


def define(module: ModuleType) -> Optional[str]:
    return module.__name__ if isinstance(module, ModuleType) and module.__name__ == "json" else None

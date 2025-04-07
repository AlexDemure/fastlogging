<p align="center">
  <a href="https://github.com/AlexDemure/fastgenerator">
    <a href="https://ibb.co/zVHLZR6Q"><img src="https://i.ibb.co/fdGKHpDq/Frame-1349-4.png" alt="Frame-1349-4" border="0"></a>
  </a>
</p>

<p align="center">
  A production-ready logging configuration module for Python.
</p>

---

## Installation

```
pip install defastlogging
```

## Usage

```python
import json
import sys
import logging
from fastlogging import config, Logger

config.setup(Logger("root", logging.INFO, json, sys.stdout))

logger = logging.getLogger()
```

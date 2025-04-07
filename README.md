<p align="center">
  <a href="https://github.com/AlexDemure/gadlogger">
    <a href="https://ibb.co/KpdqfcxH"><img src="https://i.ibb.co/ksj8wV2F/logo.png" alt="logo" border="0"></a>
  </a>
</p>

<p align="center">
  A production-ready logging configuration module for Python.
</p>

---

## Installation

```
pip install gadlogger
```

## Usage

```python
import json
import sys
import logging
from gadlogger import config, Logger

config.setup(Logger("root", logging.INFO, json, sys.stdout))

logger = logging.getLogger()
```

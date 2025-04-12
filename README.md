<p align="center">
  <a href="https://github.com/AlexDemure/gadlogging">
    <a href="https://ibb.co/VpBD9SCB"><img src="https://i.ibb.co/vvzmqPdz/logo.png" alt="logo" border="0"></a>
  </a>
</p>

<p align="center">
  A production-ready logging configuration module for Python.
</p>

---

### Installation

```
pip install gadlogging
```

### Usage

```python
import json
import sys
import logging
from gadlogging import config, Logger

config.setup(Logger("root", logging.INFO, json, sys.stdout))

logger = logging.getLogger()
```

# Exit Codes

This package is a cross-operating-system compatible version of the `os` library's EX\_\* constants.

If these constants are available, they will be re-exported directly from `os`, otherwise the integer version will be provided from this library.

This library also provides an enum version of the exit codes, if that is of value.

Apologies for the weird PyPi name, they're a bit overly restrictive and don't point to what specifically is the conflicting package.

## Installation

```shell
python -m pip install -U os-exitcodes
```

## Usage

### Constants

```python
from os_exitcodes import (
    EX_OK,
    EX_USAGE,
)
from random import choice

def is_valid_usage() -> bool:
    # check if the user is using this properly
    # for a working example, this is random
    return choice([True, False])

def main() -> None:
    invalid_usage = random
    if not is_valid_usage():
        raise SystemExit(EX_USAGE)
    raise SystemExit(EX_OK)

if __name__ == "__main__":
    main()
```

### Enumeration

```python
from os_exitcodes import ExitCode
from random import choice

def is_valid_usage() -> bool:
    # check if the user is using this properly
    # for a working example, this is random
    return choice([True, False])

def main() -> None:
    invalid_usage = random
    if not is_valid_usage():
        raise SystemExit(ExitCode.EX_USAGE)
    raise SystemExit(ExitCode.EX_OK)

if __name__ == "__main__":
    main()
```

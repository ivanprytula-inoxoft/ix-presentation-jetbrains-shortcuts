"""14: Optimize Imports

Automate the organizing and cleaning up of your Python imports with Optimize Imports.

- Problems:
    - One unused import
    - Unsorted import list, per group
    - I want multiple per line

- Optimize Imports (Ctrl-Alt-O Win/Linux/macOS)
- Undo/Redo
- Split imports  via
  ``Preferences | Editor | Code Style | Python | Imports``
  - ``Structure of "from" imports`` -> ``Always split imports``
"""
from sys import platform
import math
from sys import version
from time import time
import binascii


def e14_optimize_imports():
    print(version, platform)
    print()
    print(time())
    return 14


e14_optimize_imports()

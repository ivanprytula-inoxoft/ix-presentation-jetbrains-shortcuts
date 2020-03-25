"""18: Quick Documentation. View Parameter Info

View documentation without interrupting your flow.
- What is ``random.choice``? Stop what you're doing, get out of flow, etc.
- ``Ctrl-Q Win/Linux, Cmd-Q macOS`` on the symbol

Quickly see function arguments and argument types.
- ``choices`` is weird, what does it want?
- Put cursor in brackets of ``choices()`` and do (Ctrl-P Win/Linux, Cmd-P macOS) to see parameter list
    - Pass 1-2  parameters to see bold change to current ones
"""

from random import choice, choices

customers = ('Larry', 'Alice', 'Sam')


def e18_quick_documentation():
    customer = choice  # Not sure what this function does?
    # customer = choices()  # Not sure the parameters here

    return customer

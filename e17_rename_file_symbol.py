"""17: Rename a File and Its References. Rename Symbol

Change your mind on a file name and the IDE makes all the changes for you.
- Activate navbar, select ``models.py``
- Refactor -> Rename to ``model.py``
- See the import below is changed
- Undo to put it back

Change a variable name, class name, or other symbol, across the project.
- ``Human`` is used in many places, but we want to change to
    ``People``
- Navigate to Symbol with Cmd-B
- Shift-F6 | Rename -> ``Human``
- Ctrl-Alt-Left arrow back to code
- **** UNDO **** puts ``Human`` back everywhere
- Could also rename from here
"""

from directory_one.models import Human

programmer = Human(15)
print(Human.hands_clean)

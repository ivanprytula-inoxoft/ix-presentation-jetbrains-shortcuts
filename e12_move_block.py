"""12: Move Block Up/Down Using Keyboard

Use the keyboard to move a line or selection up or down in your file.

- The ``CONSTANT`` and ``other_string_block`` definitions
     doesn't need to be in block

- Dumb way: select line, cut, paste

- Single-line: Use Move Line Up
  # TODO: please, double check for macOS
  (Ctrl-Shift-Up/Down Win/Linux, Ctrl-Shift-Up/Down macOS)
- Block: Use keyboard to make/extend selection, then same

- *** One more useful shortcut ```Join Lines``` Ctrl-Shift-J
    ! Especially good for multi-strings
"""


def e12_move_block():
    site = 'my site'

    pi = 3.14

    other_string_block = """
        very big
        block should be
        above
        function
        """

    print(site)

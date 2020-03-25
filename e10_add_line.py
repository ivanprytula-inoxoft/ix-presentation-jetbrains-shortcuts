"""10: Add Line After/Before

Smart-add a line, from the middle of a line, after or before the current line.

- Cursor on ``very`` in the ``text`` variable below

- Start New Line (Shift-Enter Win/Linux/macOS)

- Start New Line Before Current
  (Ctrl-Alt-Enter Win/Linux, Alt-Cmd-Enter macOS)

- Or better still, Find Action | ``st be``
"""


class NewLine:
    text = 'very important message'

    def __init__(self, to_whom):
        self.to_whom = to_whom

    @staticmethod
    def e10_get_receiver_message(self):
        print(f'{self.text} for {self.to_whom}')

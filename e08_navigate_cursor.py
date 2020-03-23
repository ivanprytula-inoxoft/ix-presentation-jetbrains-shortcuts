"""08: Navigate Cursor Position Back and Forth

Easily navigate back to where you were, or where you went.

- Useful for example when debugging, chasing rabbit hole

- On `Human`, then `factorial` (Ctrl-B Win/Linux, Cmd-B on macOS)

- Use Alt-Shift-left/right to return/descend (Cmd-left/right brackets on macOS)
"""

from directory_one.models import Human


def e08_navigate_cursor(employees, current_wage):
    total_expenses = employees * current_wage
    print(f'Total expenses: ${total_expenses}')


it_man_one = Human(30)
total_money = it_man_one.get_current_wage()
e08_navigate_cursor(5, total_money)

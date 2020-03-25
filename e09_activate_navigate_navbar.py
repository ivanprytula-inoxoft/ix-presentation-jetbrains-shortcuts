"""09: Activate Navigation Bar & Navigate Files

Bring up the Navigation Bar as needed, let it disappear when finished.

- Now: Turn off Project tool window, go into full screen mode
- What if I need to *browse* files...but only *sometimes*?
- Alt-1/Cmd-1 to re-open Project Tool, then again to close? Nope.
- Jump to Navigation Bar (Alt-Home Win/Linux, Cmd-Up macOS)

Move around your project tree and select files, from your keyboard, with the Navigation Bar.
- Left, down, up
- E.g. go to e09
- Current directory doesn't need initial left

Narrow and select from a long folder listing Navigation Bar by typing a speed search.
- Activate
- Press down
- Type ``e08``
- Type ``e42`` to see items out of view

Activate the Navigation Bar and create a new file somewhere in the project tree.
- Activate, navigate to where you want to go (Alt-Insert Win/Linux, Cmd-N macOS)
- E.g. Make to-do file in root of project file
- Current directory is easy: activate, down, (Alt-Insert Win/Linux, Cmd-N macOS)

Use keyboard and Navigation Bar to find files under a path.
- Activate, up, (x2 Ctrl-Shift-F Win/Linux, Shift-Cmd-F macOS)
- Type ``Python``
- Other things you can do, e.g. refactor, copy current file

--- Hit ``Esc`` to dismiss Navigation Bar
"""


def e09_activate_navbar():
    print('Jump to Navigation Bar (Alt-Home Win/Linux, Cmd-Up macOS)')
    print('Move around your project tree and select files, from your keyboard, with the Navigation Bar')
    print('Narrow and select from a long folder listing Navigation Bar by typing a speed search.')
    print('Activate the Navigation Bar and create a new file somewhere in the project tree.')
    print('Use keyboard and Navigation Bar to find files under a path.')


if __name__ == '__main__':
    e09_activate_navbar()

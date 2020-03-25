"""15: Generate Imports While Typing, Install and import

Avoid interruption by letting PyCharm generate your imports as you type.

- We want a random customer using ``random.choice``
- Delete 'Larry'
- Wrong:
    - Go to top of file, type ``from random import choice``, go back
- Type ``cho`` and ``Ctrl-Space-Space``
- Or, type ``choice`` and ``Alt-Enter``

While typing a symbol, let PyCharm install it and generate the import.
- Cursor on maya
- Alt-Enter -> Install and import
- Then, quick fix to add to requirements.txt
"""

customers = ['Larry', 'Alice', 'Sam', ]


def e15_generate_imports():
    customer = 'Larry'  # Change to random customer
    print(maya.now())  # Fix me
    print(customer)


e15_generate_imports()

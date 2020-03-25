"""16: Adding Fields In a Constructor

Let your IDE add constructor arguments to your instance.

- Type an argument to ``__init__``

    - Wrong: manually add ``name`` and ``self.name = name``

- Alt-Enter to make it a field
"""


class Customer:
    # Pass in ``name``, store as ``self.first_name``
    def __init__(self, age, year):
        self.year = year
        self.age = age


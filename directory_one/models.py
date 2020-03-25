import math


class Human:
    current_wage: float
    legs = 2
    hands_clean = 2
    head = 1
    name = "programmer"

    def __init__(self, init_wage=10):
        self.init_wage = init_wage

    def get_current_wage(self):
        self.current_wage = math.factorial(self.init_wage / 5) * 2
        return self.current_wage

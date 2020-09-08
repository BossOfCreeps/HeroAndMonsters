from random import randint

from Bonuses.Bonus import Bonus
from constants import apple_max_value


class Apple(Bonus):
    def __init__(self, max_value=apple_max_value):
        super().__init__()

        # Check value
        if max_value > apple_max_value:
            raise Exception("Apple can't get so much health")

        # Set value
        self._value = randint(1, max_value)

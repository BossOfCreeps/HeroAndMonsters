from random import randint

from .Bonus import Bonus
from ..constants import sword_max_value


class Sword(Bonus):
    def __init__(self, max_value=sword_max_value):
        super().__init__()

        # Check value
        if max_value > sword_max_value:
            raise Exception("Sword can't get so much power")

        # Set value
        self._value = randint(1, max_value)

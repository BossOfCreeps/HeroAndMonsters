from random import randint

from Characters.Character import Character
from constants import monster_max_power, monster_max_health


class Monster(Character):
    def __init__(self, max_health=monster_max_health, max_power=monster_max_power):
        super().__init__()

        # Check values
        if max_health > monster_max_health:
            raise Exception("Monster can't be so healthy")

        if max_power > monster_max_power:
            raise Exception("Monster can't be so powerful")

        # Set values
        self._health = randint(1, max_health)
        self._power = randint(1, max_power)

import sys

from Character import Character
from Apple import Apple
from Monster import Monster
from Sword import Sword
import constants as const


class Hero(Character):
    def __init__(self):
        super().__init__()

        # Set default values
        self._health = 10
        self._power = 10
        self.__affected_monsters_counter = 0

    # Eat apple and return health
    def eat(self, apple: Apple) -> int:
        self._health += apple.value
        return self._health

    # Get sword (change power to sword value)
    def get_sword(self, sword: Sword):
        self._power = sword.value

    # Fight with monster
    def fight(self, monster: Monster):
        # Make new health
        self._health -= monster.power

        # If no more heath, death
        if self._health <= 0:
            self.__death()

        # Add monster
        self.__affected_monsters_counter += 1

        # If needed count of monsters - victory
        if self.__affected_monsters_counter == int(const.MONSTERS_COUNTER):
            self.__victory()

    # Death
    @staticmethod
    def __death():
        sys.exit(const.LOSE_STR)

    # Victory
    @staticmethod
    def __victory():
        sys.exit(const.VICTORY_STR)

    # Getters and setters

    @property
    def affected_monsters_counter(self):
        return self.__affected_monsters_counter

    @affected_monsters_counter.setter
    def affected_monsters_counter(self, value):
        raise Exception("You can set affected monsters counter")

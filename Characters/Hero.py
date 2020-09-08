import sys

from Characters.Character import Character
from Bonuses.Apple import Apple
from Characters.Monster import Monster
from Bonuses.Sword import Sword
from constants import MONSTERS_COUNTER, LOSE_STR, VICTORY_STR


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
        # Does hero can kill monster?
        if self._power < monster.health:
            self.__death()

        # Make new health
        self._health -= monster.power

        # If no more heath, death
        if self._health <= 0:
            self.__death()

        # Add monster
        self.__affected_monsters_counter += 1

        # If needed count of monsters - victory
        if self.__affected_monsters_counter == int(MONSTERS_COUNTER):
            self.__victory()

    # Death
    @staticmethod
    def __death():
        sys.exit(LOSE_STR)

    # Victory
    @staticmethod
    def __victory():
        sys.exit(VICTORY_STR)

    # Getters and setters

    @property
    def affected_monsters_counter(self):
        return self.__affected_monsters_counter

    @affected_monsters_counter.setter
    def affected_monsters_counter(self, value):
        raise Exception("You can set affected monsters counter")

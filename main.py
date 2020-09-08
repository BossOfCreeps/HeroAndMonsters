from random import randint
from time import sleep

from scripts.Bonuses.Apple import Apple
from scripts.Characters.Hero import Hero
from scripts.Characters.Monster import Monster
from scripts.Bonuses.Sword import Sword
from scripts.lib import get_decision
import scripts.constants as const


# Hero meet monster
def meet_monster(hero: Hero, monster=Monster()):
    # Notification
    print(f"\nВы встретили чудовище с {monster.health} жизнями и с силой удара {monster.power}. "
          f"Ваши здровье - {hero.health}, урон - {hero.power}")

    # Make a decision fight or pass
    decision_fight = get_decision(action=const.FIGHT_ACTION)

    # If want, make fight and notify user
    if decision_fight:
        hero.fight(monster)
        print(f"У вас осталось {hero.health} здоровья. Убито {hero.affected_monsters_counter}")


def find_sword(hero: Hero, sword=Sword()):
    # Notification
    print(f"\nВы нашли мечь. Его сила - {sword.value}. Ваша сила - {hero.power}")

    # Make a decision get sword or not
    decision_get_sword = get_decision(action=const.SWORD_ACTION)

    # If want, make
    if decision_get_sword:
        hero.get_sword(sword)


def find_apple(hero: Hero, apple=Apple()):
    # Notification and eating apple
    print(f"\nВы нашли яблоко с значением {apple.value}. Теперь ваше здоровье равно {hero.eat(apple)}")


# Main function
def main(hero=Hero()):
    # Welcome user
    print(f"Приветствую герой. У вас {hero.health} здоровья и {hero.power} силы.")

    # Gameplay
    while True:
        # Generate random event and call function of them
        event = randint(0, 2)

        if event == 0:
            meet_monster(hero, Monster())

        elif event == 1:
            find_sword(hero, Sword())

        elif event == 2:
            find_apple(hero, Apple())

        # Wait for reading text
        sleep(1)


if __name__ == '__main__':
    main()

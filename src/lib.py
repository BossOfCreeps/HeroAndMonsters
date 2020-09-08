import constants as const


def get_decision(action: str):
    """
    Return user's decision 1 or 2

    :param action: "sword" or "fight"
    :return: True or False
    """

    # Get variant string
    if action == const.FIGHT_ACTION:
        action_str = const.FIGHT_ACTION_STR

    elif action == const.SWORD_ACTION:
        action_str = const.SWORD_ACTION_STR

    else:
        raise Exception("You can decide fighting or getting sword")

    # Get data from user
    decision_ = input(f"Ваше действие {action_str}: ")

    # If data not suitable, ask return value
    if decision_ not in const.DECISION_VARIANTS:
        print("Некорректный ввод")
        return get_decision(action)

    # If data suitable return them
    else:
        return not bool(int(decision_) - 1)

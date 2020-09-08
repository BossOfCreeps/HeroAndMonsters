class Bonus:
    def __init__(self):
        self._value = None

    # Getters and setters

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value_):
        raise Exception("You can set value")

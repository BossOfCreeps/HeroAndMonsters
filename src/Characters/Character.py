class Character:
    def __init__(self):
        self._power = None
        self._health = None

    # Getters and setters

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        raise Exception("You can set health")

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        raise Exception("You can set power")

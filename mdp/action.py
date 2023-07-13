from enum import Enum


class Action(Enum):
    HIT = 0
    STICK = 1

    def __str__(self):
        return self.name.lower()

    def __eq__(self, other):
        if isinstance(other, Action):
            return self.name == other.name
        return False

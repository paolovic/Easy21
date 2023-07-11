from enum import Enum


class Action(Enum):
    HIT = 0
    STICK = 1

    def __str__(self):
        return self.name.lower()

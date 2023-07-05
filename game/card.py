from utils import *


class Card:
    def __init__(self, rng, colour=None):
        self.rng = rng
        self.value = self.value()
        if colour:
            if colour not in ['red', 'black']:
                raise ValueError("Colour must be 'red' or 'black'")
            self.colour = colour
        else:
            self.colour = self.colour()

    def value(self):
        return self.rng.randint(1, 11)

    def colour(self):
        return self.rng.choice(['red', 'black'], p=[1 / 3, 2 / 3])

    def __repr__(self):
        return f"{self.colour} {self.value}"

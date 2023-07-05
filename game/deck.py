from game.card import Card


class Deck:
    def __init__(self, rng):
        self.rng = rng

    def draw(self, colour):
        return Card(rng=self.rng, colour=colour)

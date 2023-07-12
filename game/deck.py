from game.card import Card


class Deck:
    def __init__(self, rng):
        self.rng = rng

    def draw(self, colour):
        if colour and colour not in ['red', 'black']:
            raise ValueError("Colour must be 'red' or 'black'")
        else:
            colour = self.rng.choice(['red', 'black'], p=[1 / 3, 2 / 3])
        value = self.rng.randint(1, 11)
        return Card(colour=colour, value=value)

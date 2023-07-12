from game.card import Card


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.score = 0
        self.hand = []
        self.hit(colour="black")
        self.bust = False

    def hit(self, colour=None):
        self.hand.append(self.deck.draw(colour))
        self.calculate_score()

    def calculate_score(self):
        if self.hand[-1].colour == 'red':
            self.score -= self.hand[-1].value
        else:
            self.score += self.hand[-1].value
        if self.score > 21 or self.score < 1:
            self.bust = True

    def reset(self, value):
        self.hand = [Card(colour="black", value=value)]
        self.score = value
        self.bust = False

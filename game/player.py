class Player:
    def __init__(self, name, deck):
        self.bust = None
        self.hand = None
        self.score = None
        self.name = name
        self.start(deck)

    def hit(self, deck, colour=None):
        self.hand.append(deck.draw(colour))
        self.calculate_score()
        return self.hand[-1]

    def calculate_score(self):
        if self.hand[-1].colour == 'red':
            self.score -= self.hand[-1].value
        else:
            self.score += self.hand[-1].value
        if self.score > 21 or self.score < 1:
            self.bust = True

    def start(self, deck):
        self.score = 0
        self.hand = []
        self.hit(deck,  colour="black")
        self.bust = False

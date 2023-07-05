from game.deck import Deck
from game.player import Player
from utils import *


class Game:
    def __init__(self):
        self.rng = np.random.RandomState()
        self.deck = Deck(rng=self.rng)
        self.player = Player(name="Player", deck=self.deck)
        self.dealer = Player(name="Dealer", deck=self.deck)
        self.winner = None

    def play(self):
        print("Welcome to the game of Easy21!")
        stick_or_hit = input("@{}: Do you want to stick or hit?".format(self.player.name, self.player.hand))
        while stick_or_hit != "stick":
            if stick_or_hit == "hit":
                self.player.hit(deck=self.deck)
                print("@{}: Your hand is now {}".format(self.player.name, self.player.hand))
                print("@{}: Your score is now {}".format(self.player.name, self.player.score))
                if self.player.bust:
                    print("@{}: You are bust!".format(self.player.name))
                    self.winner = self.dealer
                    break
                else:
                    stick_or_hit = input("@{}: Do you want to stick or hit?".format(self.player.name, self.player.hand))
            else:
                raise ValueError("Please enter 'stick' or 'hit'")
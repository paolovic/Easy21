from game.deck import Deck
from game.player import Player
from utils import *


class Game:
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.winner = None

    def play(self):
        print("Welcome to the game of Easy21!")
        print("The dealer's first card is {}".format(self.dealer.hand))
        print("@{}: Your hand is {}".format(self.player.name, self.player.hand))
        while not self.winner:
            self.player_turn()
            if self.winner:
                break
            self.dealer_turn()
        print("The winner is {}".format(self.winner.name))


    def player_turn(self):
        stick_or_hit = input("@{}: Do you want to stick or hit?\n".format(self.player.name, self.player.hand))
        while stick_or_hit != "stick":
            if stick_or_hit == "hit":
                self.player.hit(deck=self.deck)
                print("@{}: Your hand is now {}".format(self.player.name, self.player.hand))
                print("@{}: Your score is now {}".format(self.player.name, self.player.score))
                if self.player.bust:
                    print("@{}: You are bust!".format(self.player.name))
                    self.winner = self.dealer
                    break
                elif self.player.score == 21:
                    print("@{}: You have 21!".format(self.player.name))
                    self.winner = self.player
                    break
                else:
                    stick_or_hit = input(
                        "@{}: Do you want to stick or hit?\n".format(self.player.name, self.player.hand))
            else:
                raise ValueError("Please enter 'stick' or 'hit'")

    def dealer_turn(self):
        print("The dealer's hand is now {}".format(self.dealer.hand))
        print("The dealer's score is now {}".format(self.dealer.score))
        while self.dealer.score < 17:
            self.dealer.hit(deck=self.deck)
            print("The dealer's hand is now {}".format(self.dealer.hand))
            print("The dealer's score is now {}".format(self.dealer.score))
            if self.dealer.bust:
                print("The dealer is bust!")
                self.winner = self.player
                break
        if not self.winner:
            print("The dealer has decided to stick")
            print("The dealer's final score is {}".format(self.dealer.score))
            self.winner = self.player if self.player.score > self.dealer.score else self.dealer

    def restart(self):
        self.winner = None
        self.dealer.start(deck=self.deck)
        self.player.start(deck=self.deck)

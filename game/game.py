import utils
from game.deck import Deck
from game.player import Player


class Game:
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.winner = None

    def play(self):
        self.print_welcome_message()
        self.print_initial_game_state()
        while not self.winner:
            self.player_turn()
            if self.winner:
                break
            self.dealer_turn()
        self.print_winner()

    def player_turn(self):
        stick_or_hit = self.print_stick_or_hit_message(self.player)
        while stick_or_hit != "stick":
            if stick_or_hit == "hit":
                self.player.hit(deck=self.deck)
                self.print_current_game_state(self.player)
                if self.player.bust:
                    self.print_bust_message(self.player)
                    self.winner = self.dealer
                    break
                elif self.player.score == 21:
                    self.print_final_score(self.player)
                    self.winner = self.player
                    break
                else:
                    stick_or_hit = self.print_stick_or_hit_message(self.player)
            else:
                raise ValueError("Please enter 'stick' or 'hit'")

    def dealer_turn(self):
        while self.dealer.score < 17:
            self.print_decision_message(self.dealer, "hit")
            self.dealer.hit(deck=self.deck)
            self.print_current_game_state(self.dealer)
            if self.dealer.bust:
                self.print_bust_message(self.dealer)
                self.winner = self.player
                break
        if not self.winner:
            self.print_decision_message(self.dealer, "stick")
            self.print_final_score(self.dealer)
            self.winner = self.player if self.player.score > self.dealer.score else self.dealer

    def restart(self):
        self.winner = None
        self.dealer.start(deck=self.deck)
        self.player.start(deck=self.deck)

    def print_final_score(self, player):
        print(f"The {player.name}'s final score is {player.score}")

    def print_welcome_message(self):
        print("Welcome to the game of Easy21!")

    def print_initial_game_state(self):
        print(f"The dealer's first card is {self.dealer.hand}")
        print(f"@{self.player.name}: Your hand is {self.player.hand}")

    def print_winner(self):
        print("The winner is {}".format(self.winner.name))

    def print_stick_or_hit_message(self, player):
        return input(f"@{player.name}: Do you want to stick or hit?\n")

    def print_current_game_state(self, player):
        print(f"The {player.name}'s hand is now {player.hand}")
        print(f"The {player.name}'s score is now {player.score}")

    def print_decision_message(self, player, decision):
        print(f"The {player.name} has decided to {decision}")

    def print_bust_message(self, player):
        print(f"The {player.name} is bust!")
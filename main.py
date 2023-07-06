from game.game import Game
from game.deck import Deck
from game.player import Player
from utils import *

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rng = np.random.RandomState()
    deck = Deck(rng=rng)
    player = Player(name="Player", deck=deck)
    dealer = Player(name="Dealer", deck=deck)
    game = Game(deck=deck, player=player, dealer=dealer)
    while True:
        game.play()
        play_again = input("Do you want to play again? (y/n)\n")
        if play_again == "n":
            break
        elif play_again == "y":
            game.restart()
        else:
            raise ValueError("Please enter 'y' or 'n'")

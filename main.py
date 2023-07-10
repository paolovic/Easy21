from game.game import Game
from game.deck import Deck
from game.player import Player
from mdp.state import State
from utils import *

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rng = np.random.RandomState()
    deck = Deck(rng=rng)
    player = Player(name="Player", deck=deck)
    dealer = Player(name="Dealer", deck=deck)
    state = State(players_sum=player.hand[0].value, dealers_first_card=dealer.hand[0].value, terminal=False)
    game = Game(deck=deck, state=state, player=player, dealer=dealer)
    while True:
        game.play()
        play_again = input("Do you want to play again? (y/n)\n")
        if play_again == "n":
            break
        elif play_again == "y":
            player.start()
            dealer.start()
            state = State(players_sum=player.hand[0].value, dealers_first_card=dealer.hand[0].value, terminal=False)
            game.restart(state=state)
        else:
            raise ValueError("Please enter 'y' or 'n'")

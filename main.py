from game.game import Game
from game.deck import Deck
from game.player import Player
import numpy as np
import matplotlib.pyplot as plt


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def draw_action_value_function(opt_val_f):
    # Assuming optimal_value_function is your optimal value function array with shape (10, 21)
    # Create x, y, z values for the 3D plot
    x = np.arange(1, 11)  # Dealer's first card showing
    y = np.arange(1, 22)  # Player's sum
    x, y = np.meshgrid(x, y)
    z = opt_val_f[x - 1, y - 1]

    # Plot the 3D surface
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z)
    ax.set_xlabel('Dealer Showing')
    ax.set_ylabel('Player Sum')
    ax.set_zlabel('Optimal Value')
    ax.set_title('Optimal Value Function V*(s)')

    # Show the plot
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rng = np.random.RandomState()
    deck = Deck(rng=rng)
    player = Player(name="Player", deck=deck)
    dealer = Player(name="Dealer", deck=deck)
    # state = State(dealers_first_card=dealer.hand[0].value, players_sum=player.hand[0].value, terminal=False)
    game = Game(deck=deck, player=player, dealer=dealer, rng=rng)
    action_value_function = game.on_policy_monte_carlo_control(episodes=1000000)
    optimal_value_function = np.max(action_value_function, axis=2)
    draw_action_value_function(opt_val_f=optimal_value_function)
    """while True:
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
            raise ValueError("Please enter 'y' or 'n'")"""

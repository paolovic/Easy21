class State:
    def __init__(self, dealers_first_card, players_sum, terminal):
        self.dealer_showing = dealers_first_card
        self.player_sum = players_sum
        self.terminal = terminal

    def __repr__(self):
        return f"State(dealer_showing={self.dealer_showing}, player_sum={self.player_sum}, terminal={self.terminal})"

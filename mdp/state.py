class State:
    def __init__(self, dealers_first_card, players_sum, terminal):
        self.dealer_showing = dealers_first_card
        self.player_sum = players_sum
        self.terminal = terminal

    def __repr__(self):
        return f"State(dealer_showing={self.dealer_showing}, player_sum={self.player_sum}, terminal={self.terminal})"

    def __eq__(self, other):
        if isinstance(other, State):
            return self.dealer_showing == other.dealer_showing and self.player_sum == other.player_sum and self.terminal == other.terminal
        return False

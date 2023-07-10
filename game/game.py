from mdp.action import Action
from mdp.reward import Reward
from mdp.state import State


class Game:
    def __init__(self, deck, state, player, dealer):
        self.reward = None
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.state = state
        self.print_welcome_message()
        self.print_current_game_state()

    def step(self, state, action):
        if action is Action.HIT:
            self.player.hit()
        else:
            self.dealer_turn()
        new_state = self.calculate_state(state)
        reward = self.calculate_reward(new_state)
        return new_state, reward

    def calculate_state(self, state):
        new_state = State(dealers_first_card=state.dealers_first_card, players_sum=self.player.score,
                          terminal=(self.player.bust or self.dealer.bust or state.terminal))
        return new_state

    def calculate_reward(self, state):
        if state.terminal:
            if self.player.bust:
                return Reward.LOSE
            elif self.dealer.bust:
                return Reward.WIN
            elif self.player.score > self.dealer.score:
                return Reward.WIN
            elif self.player.score < self.dealer.score:
                return Reward.LOSE
            else:
                return Reward.DRAW
        else:
            return Reward.DRAW

    def dealer_turn(self):
        while self.dealer.score < 17:
            self.print_decision_message(self.dealer, "hit")
            self.dealer.hit()
            self.print_current_game_state()
            if self.dealer.bust:
                self.print_bust_message(self.dealer)
                return
        self.print_decision_message(self.dealer, "stick")
        self.state.terminal = True

    def play(self):
        while not self.state.terminal:
            action = self.print_stick_or_hit_message(self.player)
            next_state, reward = self.step(self.state, action)
            self.state = next_state
            self.print_current_game_state()
            self.reward = reward
        self.print_winner(self.reward)

    def restart(self, state):
        self.state = state
        self.print_welcome_message()
        self.print_current_game_state()

    def print_final_score(self, player):
        print(f"The {player.name}'s final score is {player.score}")

    def print_welcome_message(self):
        print("Welcome to the game of Easy21!")

    def print_winner(self, reward):
        if reward is Reward.WIN:
            print("The winner is {}".format(self.player.name))
        elif reward is Reward.LOSE:
            print("The winner is {}".format(self.dealer.name))

    def print_stick_or_hit_message(self, player):
        answer = input(f"@{player.name}: Do you want to stick or hit?\n")
        if answer != "stick" and answer != "hit":
            raise ValueError("Please enter 'hit' or 'stick'")
        self.print_decision_message(player, answer)
        if answer == "hit":
            return Action.HIT
        else:
            return Action.STICK

    def print_current_game_state(self):
        print(f"The dealer's first card is worth {self.state.dealers_first_card}")
        print(f"@{self.player.name}: Your hand is worth {self.state.players_sum}")

    def print_decision_message(self, player, decision):
        print(f"The {player.name} has decided to {decision}")

    def print_bust_message(self, player):
        print(f"The {player.name} is bust!")

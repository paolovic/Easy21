from mdp.action import Action
from mdp.state import State
import numpy as np


class Game:
    def __init__(self, deck, player, dealer, rng):
        self.state = None
        self.reward = None
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.rng = rng
        self.print_welcome_message()

    def step(self, state, action):
        self.print_decision_message(self.player, action)
        if action is Action.HIT:
            self.player.hit()
        else:
            self.dealer_turn()
            state.terminal = True
        next_state = self.calculate_state(state)
        reward = self.calculate_reward(next_state)
        self.state = next_state
        self.print_current_game_state()
        print(f"Immediate Reward: {reward}")
        print(f"Next state: {next_state}")
        return next_state, reward

    def monte_carlo_es(self, episodes):
        # initialise
        policy = self.rng.choice([Action.HIT, Action.STICK], size=(10, 21))
        action_value_function = np.zeros((10, 21, 2))
        returns = np.zeros((10, 21, 2))
        # count the number of times s is visited
        N = np.zeros((10, 21, 2))
        # loop forever for each episode
        for episode in range(episodes):
            # choose S_0 randomly
            self.player.reset(value=self.rng.randint(1, 22))
            self.dealer.reset(value=self.rng.randint(1, 11))
            S_0 = State(dealers_first_card=self.dealer.score, players_sum=self.player.score,
                        terminal=False)
            # choose A_0 randomly
            A_0 = self.rng.choice([Action.HIT, Action.STICK])
            # generate an episode starting from S_0, A_0, following pi
            episode = self.generate_episode(S_0, A_0, policy)
            G = 0
            # loop for each step of episode, t = T-1, T-2, ..., 0
            for t in range(len(episode) - 1, -1, -1):
                gamma = 1
                # G = R_t+1 + gamma * G
                G = episode[t][2] + gamma * G
                # unless s_t, a_t appears in S_0, A_0, s_1, a_1, ..., s_t-1, a_t-1:
                s_t = episode[t][0]
                a_t = episode[t][1]
                if (s_t, a_t) not in [(x[0], x[1]) for x in episode[:t]]:
                    # returns(s_t, a_t) = returns(s_t, a_t) + G
                    returns[s_t.dealer_showing - 1, s_t.player_sum - 1, a_t.value] += G
                    # count the number of times s_t is visited
                    N[s_t.dealer_showing - 1, s_t.player_sum - 1, a_t.value] = N[
                                                                                   s_t.dealer_showing - 1, s_t.player_sum - 1, a_t.value] + 1
                    # Q(s_t, a_t) = average(returns(s_t, a_t))
                    action_value_function[s_t.dealer_showing - 1, s_t.player_sum - 1, a_t.value] = \
                        returns[s_t.dealer_showing - 1, s_t.player_sum - 1, a_t.value] / \
                        N[s_t.dealer_showing - 1, s_t.player_sum - 1, a_t.value]
                    # pi(s_t) = argmax_a(Q(s_t, a))
                    policy[s_t.dealer_showing - 1, s_t.player_sum - 1] = Action(np.argmax(
                        action_value_function[s_t.dealer_showing - 1, s_t.player_sum - 1, :]))
        return action_value_function

    def generate_episode(self, state, action, policy):
        episode = []
        while True:
            next_state, reward = self.step(state, action)
            episode.append((state, action, reward))
            if next_state.terminal:
                break
            action = policy[next_state.dealer_showing - 1, next_state.player_sum - 1]
            state = next_state
        return episode

    def calculate_state(self, state):
        return State(dealers_first_card=state.dealer_showing, players_sum=self.player.score,
                     terminal=(self.player.bust or self.dealer.bust or state.terminal))

    def calculate_reward(self, state):
        if state.terminal:
            if self.player.bust:
                return -1
            elif self.dealer.bust:
                return 1
            elif self.player.score < self.dealer.score:
                return -1
            elif self.player.score > self.dealer.score:
                return 1
            else:
                return 0
        else:
            return 0

    def dealer_turn(self):
        while self.dealer.score < 17:
            self.print_decision_message(self.dealer, Action.HIT)
            self.dealer.hit()
            if self.dealer.bust:
                self.print_bust_message(self.dealer)
                break
        if not self.dealer.bust:
            self.print_decision_message(self.dealer, Action.STICK)

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
        if reward > 0:
            print(f"The winner is {self.player.name}")
        elif reward < 0:
            print(f"The winner is {self.dealer.name}")
        else:
            print("It's a draw!")

    def print_stick_or_hit_message(self, player):
        answer = input(f"@{player.name}: Do you want to stick or hit?\n")
        if answer != "stick" and answer != "hit":
            raise ValueError("Please enter 'hit' or 'stick'")
        if answer == "hit":
            return Action.HIT
        else:
            return Action.STICK

    def print_current_game_state(self):
        print(f"The dealer's first card is worth {self.state.dealer_showing}")
        print(f"@{self.player.name}: Your hand is worth {self.state.player_sum}")

    def print_decision_message(self, player, decision):
        print(f"The {player.name} has decided to {decision}")

    def print_bust_message(self, player):
        print(f"The {player.name} is bust!")

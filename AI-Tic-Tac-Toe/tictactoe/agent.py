from abc import ABC, abstractmethod
import os
import pickle
import collections
import numpy as np
import random
class Learner(ABC):
    """
    Parent class for Q-learning and SARSA agents.

    Parameters
    ----------
    alpha : float 
        learning rate
    gamma : float
        temporal discounting rate
    eps : float 
        probability of random action vs. greedy action
    eps_decay : float
        epsilon decay rate. Larger value = more decay
    """
    def __init__(self, alpha, gamma, eps, eps_decay=0.):
        # Agent parameters
        self.alpha = alpha
        self.gamma = gamma
        self.eps = eps
        self.eps_decay = eps_decay
        # Possible actions correspond to the set of all x,y coordinate pairs
        self.actions = []
        for i in range(3):
            for j in range(3):
                self.actions.append((i,j))
        # Initialize Q values to 0 for all state-action pairs.
        # Access value for action a, state s via Q[a][s]
        self.Q = {}
        for action in self.actions:
            self.Q[action] = collections.defaultdict(int)
        # Keep a list of reward received at each episode
        self.rewards = []

    def get_action(self, s, difficulty='hard'):
        possible_actions = [a for a in self.actions if s[a[0] * 3 + a[1]] == '-']

        if difficulty == 'easy':
            # Always choose randomly
            action = random.choice(possible_actions)

        elif difficulty == 'medium':
            if random.random() < 0.5:
                # 50% chance: random
                action = random.choice(possible_actions)
            else:
                # 50% chance: greedy
                values = np.array([self.Q[a][s] for a in possible_actions])
                max_val = np.max(values)
                max_indices = np.where(values == max_val)[0]
                ix_select = np.random.choice(max_indices)
                action = possible_actions[ix_select]

        else:  # hard
            values = np.array([self.Q[a][s] for a in possible_actions])
            max_val = np.max(values)
            max_indices = np.where(values == max_val)[0]
            ix_select = np.random.choice(max_indices)
            action = possible_actions[ix_select]

        self.eps *= (1. - self.eps_decay)
        return action

    def save_agent(self, path):
        """ Pickle the agent object instance to save the agent's state. """
        if os.path.isfile(path):
            os.remove(path)
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @abstractmethod
    def update(self, s, s_, a, a_, r):
        pass


class Qlearner(Learner):
    """
    A class to implement the Q-learning agent.
    """
    def __init__(self, alpha, gamma, eps, eps_decay=0.):
        super().__init__(alpha, gamma, eps, eps_decay)

    def update(self, s, s_, a, a_, r):
        """
        Perform the Q-Learning update of Q values.

        Parameters
        ----------
        s : string
            previous state
        s_ : string
            new state
        a : (i,j) tuple
            previous action
        a_ : (i,j) tuple
            new action. NOT used by Q-learner!
        r : int
            reward received after executing action "a" in state "s"
        """
        # Update Q(s,a)
        if s_ is not None:
            # hold list of Q values for all a_,s_ pairs. We will access the max later
            possible_actions = [action for action in self.actions if s_[action[0]*3 + action[1]] == '-']
            Q_options = [self.Q[action][s_] for action in possible_actions]
            # update
            self.Q[a][s] += self.alpha*(r + self.gamma*max(Q_options) - self.Q[a][s])
        else:
            # terminal state update
            self.Q[a][s] += self.alpha*(r - self.Q[a][s])

        # add r to rewards list
        self.rewards.append(r)


class SARSAlearner(Learner):
    """
    A class to implement the SARSA agent.
    """
    def __init__(self, alpha, gamma, eps, eps_decay=0.):
        super().__init__(alpha, gamma, eps, eps_decay)

    def update(self, s, s_, a, a_, r):
        """
        Perform the SARSA update of Q values.

        Parameters
        ----------
        s : string
            previous state
        s_ : string
            new state
        a : (i,j) tuple
            previous action
        a_ : (i,j) tuple
            new action
        r : int
            reward received after executing action "a" in state "s"
        """
        # Update Q(s,a)
        if s_ is not None:
            self.Q[a][s] += self.alpha*(r + self.gamma*self.Q[a_][s_] - self.Q[a][s])
        else:
            # terminal state update
            self.Q[a][s] += self.alpha*(r - self.Q[a][s])

        # add r to rewards list
        self.rewards.append(r)

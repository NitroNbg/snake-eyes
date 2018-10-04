from typing import TypeVar, Generic
import random
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from memory import ReplayMemory
from memory import Transition
from hyperparameters import EPS_START
from hyperparameters import EPS_END
from hyperparameters import EPS_DECAY
State = TypeVar('State')

GAMMA = 0.9


class DeepQNetwork(nn.Module):
    """Class that contains the logic for data crunching"""

    def __init__(self, input_size):
        super(DeepQNetwork, self).__init__()
        n_hidden = 10
        self.initial = nn.Linear(input_size, n_hidden)
        self.hidden = nn.Linear(n_hidden, n_hidden)
        self.out = nn.Linear(n_hidden, 4)

    def forward(self, input_param):
        intermediate = F.relu(self.initial(input_param))
        intermediate = F.relu(self.hidden(intermediate))
        return self.out(intermediate)


class LearningAgent(Generic[State]):
    """Base class for learning agents containing the basic fields and method definitions"""

    def __init__(self, input_size, capacity, device):
        self.player_index = -1
        self.capacity = capacity
        self.device = device
        self.policy_net = DeepQNetwork(input_size).to(device)
        self.target_net = DeepQNetwork(input_size).to(device)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()
        self.optimizer = optim.RMSprop(self.policy_net.parameters())
        self.memory = ReplayMemory(capacity=capacity)

    def __str__(self):
        return "LearningAgent"

    def play(self, state, turn):
        sample = random.random()
        eps_threshold = EPS_END + (EPS_START - EPS_END) * math.exp(-1 * turn / EPS_DECAY)
        if sample > eps_threshold:
            with torch.no_grad():
                return self.policy_net(state.to_tensor()).max(0)[1]
        else:
            return torch.Tensor([[random.randrange(4)]], device=self.device)

    def optimize(self):
        transitions = self.memory.sample(500)
        normalized_transitions = Transition(*zip(*transitions))

    def set_index(self, index):
        self.player_index = index

    def extrapolate_state(self, snake, snakes, food, grid):
        raise NotImplementedError("extrapolate_state not implemented")

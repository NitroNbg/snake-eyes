from typing import TypeVar, Generic
import random
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from hyperparameters import EPS_START
from hyperparameters import EPS_END
from hyperparameters import EPS_DECAY
State = TypeVar('State')


class DeepQNetwork(nn.Module):
    """Class that contains the logic for data crunching"""

    def __init__(self):
        super(DeepQNetwork, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=5, stride=2)
        self.bn1 = nn.BatchNorm2d(16)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=5, stride=2)
        self.bn2 = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=5, stride=2)
        self.bn3 = nn.BatchNorm2d(32)
        self.out = nn.Linear(448, 4)

    def forward(self, input_param):
        intermediate = F.relu(self.bn1(self.conv1(input_param)))
        intermediate = F.relu(self.bn2(self.conv2(intermediate)))
        intermediate = F.relu(self.bn3(self.conv3(intermediate)))
        return self.out(intermediate.view(intermediate.size(0), -1))


class LearningAgent(Generic[State]):
    """Base class for learning agents containing the basic fields and method definitions"""

    def __init__(self, capacity, device):
        self.memory = []
        self.capacity = capacity
        self.device = device
        self.policy_net = DeepQNetwork().to(device)
        self.target_net = DeepQNetwork().to(device)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()

    def play(self, state, turn, device='cpu'):
        sample = random.random()
        eps_threshold = EPS_END + (EPS_START - EPS_END) * math.exp(-1 * turn / EPS_DECAY)
        if sample > eps_threshold:
            with torch.no_grad():
                return self.policy_net(state).max(1)[1].view(1, 1)
        else:
            return torch.Tensor([[random.randrange(4)]], device=device, dtype=torch.Tensor.long())

    def extrapolate_state(self, snake, snakes, food, grid):
        return

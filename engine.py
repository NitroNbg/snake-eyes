import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib
import matplotlib.pyplot as pypl

is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)


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

    def forward(self, input):
        intermediate = F.relu(self.bn1(self.conv1(input)))
        intermediate = F.relu(self.bn2(self.conv2(intermediate)))
        intermediate = F.relu(self.bn3(self.conv3(intermediate)))
        return self.out(intermediate.view(intermediate.size(0), -1))


class Plotter:
    """Plotter class that helps with logging the progress of the training"""
    episode_durations = []

    def plot_durations(self):
        pypl.figure(2)
        pypl.clf()
        durations_t = torch.tensor(Plotter.episode_durations, torch.float)
        pypl.title('Training...')
        pypl.xlabel('Episode')
        pypl.ylabel('Duration')
        pypl.plot(durations_t.numpy())
        if len(durations_t) >= 100:
            means = durations_t.unfold(0, 100, 1).mean(1).view(-1)
            means = torch.cat((torch.zeros(99), means))
            pypl.plot(means.numpy())

        pypl.pause(0.001)
        if is_ipython:
            display.clear_output(True)
            display.display(pypl.gcf())

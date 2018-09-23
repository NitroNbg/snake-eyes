from learning_agent import LearningAgent
from state import HeadOnlyState


class HeadAndFoodAgent(LearningAgent[HeadOnlyState]):

    def __init__(self):
        super(LearningAgent, self).__init__()
        self.memory.printSelf()
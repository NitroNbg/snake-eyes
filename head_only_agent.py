from learning_agent import LearningAgent


class HeadOnlyAgent(LearningAgent[str]):

    def __init__(self):
        print('HeadOnlyAgent init')
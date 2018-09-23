from typing import TypeVar, Generic
State = TypeVar['State']


class LearningAgent(Generic[State]):
    """Base class for learning agents containing the basic fields and method definitions"""

    def __init__(self):
        self.memory = []

    def __index__(self, capacity):
        self.memory = []
        self.capacity = capacity

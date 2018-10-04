import torch


class State:
    def __init__(self):
        self.isTerminal = False

    def printSelf(self):
        print('printSelf')

    def to_tensor(self):
        raise NotImplementedError("to_tensor() not implemented")


class HeadOnlyState(State):
    def __init__(self):
        super(State, self).__init__()
        self.top = 0
        self.right = 0
        self.down = 0
        self.left = 0

    def printSelf(self):
        print("HeadOnlyState (top=%d, right=%d, down=%d, left=%d" % (self.top, self.right, self.down, self.left))

    def to_tensor(self):
        return torch.FloatTensor([self.top, self.right, self.down, self.left])


class HeadAndAbsoluteFoodState(State):
    def __init__(self):
        super(State, self).__init__()
        self.top = 0
        self.right = 0
        self.down = 0
        self.left = 0
        self.food = [0, 0]  # absolute x, y position of the food, uses natural coordinate system; (0, 0) is top left

    def printSelf(self):
        print("HeadAndAbsoluteFoodState (top=%d, right=%d, down=%d, left=%d, food=%s" % (self.top, self.right, self.down, self.left, self.food))

    def to_tensor(self):
        return torch.FloatTensor([self.top, self.right, self.down, self.left, self.food[0], self.food[1]])


class HeadAndDistanceToFoodState(State):
    def __init__(self):
        super(State, self).__init__()
        self.top = 0
        self.right = 0
        self.down = 0
        self.left = 0
        self.dfood = [0, 0]  # relative distance [x, y] to the food

    def printSelf(self):
        print("HeadAndDistanceToFoodState (top=%d, right=%d, down=%d, left=%d, dfood=%s" % (self.top, self.right, self.down, self.left, self.dfood))

    def to_tensor(self):
        return torch.FloatTensor([self.top, self.right, self.down, self.left, self.dfood[0], self.dfood[1]])

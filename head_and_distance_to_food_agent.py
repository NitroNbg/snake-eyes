from learning_agent import LearningAgent
from state import HeadAndDistanceToFoodState
import numpy as np


class HeadAndDistanceToFoodAgent(LearningAgent[HeadAndDistanceToFoodState]):

    def __init__(self, device):
        super(HeadAndDistanceToFoodAgent, self).__init__(input_size=6, capacity=1000, device=device)

    def __str__(self):
        return "[HeadAndDistanceToFoodAgent]"

    def extrapolate_state(self, snake, snakes, food, grid):
        found = False
        left_obstacle = [snake.head[0], snake.head[1]]
        while not found and left_obstacle[0] > 0:
            left_obstacle = [left_obstacle[0] - 1, snake.head[1]]
            for i in range(0, len(snakes)):
                if snake.head[0] != snakes[i].head[0] or snake.head[1] != snakes[i].head[1]:
                    found = found or np.any(snakes[i].body == left_obstacle)
        min_left = snake.head[0] - left_obstacle[0]
        found = False
        right_obstacle = [snake.head[0], snake.head[1]]
        while not found and right_obstacle[0] < grid[0]:
            right_obstacle = [right_obstacle[0] + 1, snake.head[1]]
            for i in range(0, len(snakes)):
                if snake.head[0] != snakes[i].head[0] or snake.head[1] != snakes[i].head[1]:
                    found = found or np.any(snakes[i].body == right_obstacle)
        min_right = right_obstacle[0] - snake.head[0]
        found = False
        top_obstacle = [snake.head[0], snake.head[1]]
        while not found and top_obstacle[1] > 0:
            top_obstacle = [snake.head[0], top_obstacle[1] - 1]
            for i in range(0, len(snakes)):
                if snake.head[0] != snakes[i].head[0] or snake.head[1] != snakes[i].head[1]:
                    found = found or np.any(snakes[i].body == top_obstacle)
        min_top = snake.head[1] - top_obstacle[1]
        found = False
        bottom_obstacle = [snake.head[0], snake.head[1]]
        while not found and bottom_obstacle[1] < grid[1]:
            bottom_obstacle = [snake.head[0], bottom_obstacle[1] + 1]
            for i in range(0, len(snakes)):
                if snake.head[0] != snakes[i].head[0] or snake.head[1] != snakes[i].head[1]:
                    found = found or np.any(snakes[i].body == bottom_obstacle)
        min_bottom = bottom_obstacle[1] - snake.head[1]
        state = HeadAndDistanceToFoodState()
        state.top = min_top
        state.right = min_right
        state.down = min_bottom
        state.left = min_left
        dfoodx = food[0] - snake.head[0]
        dfoody = food[1] - snake.head[1]
        state.dfood = [dfoodx, dfoody]
        return state

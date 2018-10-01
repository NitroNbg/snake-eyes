from learning_agent import LearningAgent
from state import HeadAndAbsoluteFoodState


class HeadAndFoodAgent(LearningAgent[HeadAndAbsoluteFoodState]):

    def __init__(self):
        super(LearningAgent, self).__init__()
        self.memory.printSelf()

    def extrapolate_state(self, snake, snakes, food, grid):
        found = False
        left_obstacle = [snake.head.x, snake.head.y]
        while not found and left_obstacle[0] > 0:
            left_obstacle = [left_obstacle[0] - 1, snake.head.y]
            for i in range(0, len(snakes)):
                if snake.head.x != snakes[i].head.x or snake.head.y != snakes[i].head.y:
                    found = found or left_obstacle in snakes[i].body
        min_left = snake.head.x - left_obstacle[0]
        found = False
        right_obstacle = [snake.head.x, snake.head.y]
        while not found and right_obstacle[0] < grid.x:
            right_obstacle = [right_obstacle[0] + 1, snake.head.y]
            for i in range(0, len(snakes)):
                if snake.head.x != snakes[i].head.x or snake.head.y != snakes[i].head.y:
                    found = found or right_obstacle in snakes[i].body
        min_right = right_obstacle[0] - snake.head.x
        found = False
        top_obstacle = [snake.head.x, snake.head.y]
        while not found and top_obstacle[1] > 0:
            top_obstacle = [snake.head.x, top_obstacle[1] - 1]
            for i in range(0, len(snakes)):
                if snake.head.x != snakes[i].head.x or snake.head.y != snakes[i].head.y:
                    found = found or top_obstacle in snakes[i].body
        min_top = snake.head.y - top_obstacle[1]
        found = False
        bottom_obstacle = [snake.head.x, snake.head.y]
        while not found and bottom_obstacle[0] < grid.y:
            bottom_obstacle = [snake.head.x, bottom_obstacle[1] + 1]
            for i in range(0, len(snakes)):
                if snake.head.x != snakes[i].head.x or snake.head.y != snakes[i].head.y:
                    found = found or bottom_obstacle in snakes[i].body
        min_bottom = bottom_obstacle[1] - snake.head.y
        state = HeadOnlyState.__init__()
        state.top = min_top
        state.right = min_right
        state.down = min_bottom
        state.left = min_left
        state.food = [food.x, food.y]
        return state

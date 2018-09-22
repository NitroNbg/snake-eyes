import gym
import gym_snake

# Construct Environment
env = gym.make('snake-v0')
# Configure Environment
env.n_foods = 1
env.n_snakes = 2
env.snake_size = 4
env.unit_gap = 1
env.unit_size = 10
env.grid_size = [50, 50]
observation = env.reset() # Constructs an instance of the game

# Controller
game_controller = env.controller

# Grid
grid_object = game_controller.grid
grid_pixels = grid_object.grid

# Snake(s)
snakes_array = game_controller.snakes
snake_agent = snakes_array[0]

for step in range(1, 1000):
	env.render()
	env.step(step % 4)

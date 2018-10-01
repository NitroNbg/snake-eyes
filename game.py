import gym
import gym_snake
import snakes
from head_only_agent import HeadOnlyAgent
from head_and_food_agent import HeadAndFoodAgent
from head_and_distance_to_food_agent import HeadAndDistanceToFoodAgent

global run_with_graphics

# Construct Environment
env = gym.make('snake-v0')
# Configure Environment
env.n_foods = 1
env.n_snakes = 3
env.snake_size = 4
env.unit_gap = 1
env.unit_size = 10
env.grid_size = [60, 60]

# Controller
game_controller = env.controller

# Grid
grid_object = game_controller.grid
grid_pixels = grid_object.grid

# Snake(s)
snakes.init_snakes(game_controller.snakes)

# Agents
agents_playing = [HeadOnlyAgent.__init__(), HeadAndFoodAgent.__init__(), HeadAndDistanceToFoodAgent.__init__()]


def number_of_players():
    return env.n_snakes


def available_snake():
    return snakes.available_snake()


def add_agent(agent):
    global agents_playing
    agents_playing.append(agent)


def start_simulation():
    for episodes in range(1, 1000):
        snakes_alive = number_of_players()
        observation = env.reset()
        turn = 0
        cumulative_reward = [0] * snakes_alive
        terminated = False
        while not terminated:
            action = []
            for i in range(0, number_of_players()):
                if snakes.is_snake_alive(i):
                    state = agents_playing[i].extrapolate_state(snakes.get_snakes)
                    action[i] = agents_playing[i].play(state=state, turn=turn)
            observation = env.step(action)
            turn = turn + 1
            for i in range(0, len(observation)):
                cumulative_reward[i] = cumulative_reward[i] + observation[i]
                if observation[i] == -1:
                    print("Snake #%d died after turn %d with %d points." % (i, turn, cumulative_reward[i]))
            if run_with_graphics:
                env.render()

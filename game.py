import gym
import gym_snake
import random
import snakes
from learning_agent import GAMMA


run_with_graphics = False
# Construct Environment
env = gym.make('snake-v0')
# Configure Environment
env.n_foods = 10
env.n_snakes = 3
env.snake_size = 4
env.unit_gap = 1
env.unit_size = 10
env.grid_size = [60, 60]
observation = env.reset()

# Controller
game_controller = env.controller

# Grid
grid_object = game_controller.grid
grid_pixels = grid_object.grid

# Snake(s)
snakes.init_snakes(game_controller.snakes)

# Agents
agents_playing = []
agent_snake_pair = {}


def set_run_with_graphics(val):
    global run_with_graphics
    run_with_graphics = val


def number_of_players():
    return env.n_snakes


def available_snake():
    return snakes.available_snake()


def add_agent(agent):
    global agents_playing
    agents_playing.append(agent)


def start_simulation():
    global run_with_graphics
    global agents_playing
    global env
    global observation
    for episodes in range(1, 1000):
        snakes_alive = number_of_players()
        snakes.reset_snake_life()
        for i in range(0, number_of_players()):
            agent_snake_pair[available_snake()] = agents_playing[i]
        observation = env.reset()
        turn = 0
        cumulative_reward = [0] * snakes_alive
        terminated = False
        print("------------------------------------------------------------------------------------")
        while not terminated:
            action = [-1] * number_of_players()
            for i in range(0, number_of_players()):
                if snakes.is_snake_alive(i):
                    agent = agent_snake_pair[snakes.snakes[i]]
                    food = [random.randint(0, env.grid_size[0]), random.randint(0, env.grid_size[1])]
                    state = agent.extrapolate_state(snake=snakes.snakes[i], snakes=snakes.snakes, food=food, grid=env.grid_size)
                    action[i] = agent.play(state=state, turn=turn)
            observation, reward, done, info = env.step(action)
            turn = turn + 1
            for i in range(0, len(reward)):
                cumulative_reward[i] = GAMMA * cumulative_reward[i] + reward[i]
                if reward[i] == -1:
                    print("Snake #%d died after turn %d with %d points." % (i, turn, cumulative_reward[i]))
                    snakes.kill_snake(i)
                    terminated = snakes.terminated()
            if run_with_graphics:
                env.render()

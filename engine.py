import sys
import datetime
import game
import torch
from head_only_agent import HeadOnlyAgent
from head_and_food_agent import HeadAndFoodAgent
from head_and_distance_to_food_agent import HeadAndDistanceToFoodAgent

global run_with_graphics
global log_to_file
global log_filename

if len(sys.argv) < 2:
    run_with_graphics = False
    log_to_file = False
else:
    run_with_graphics = sys.argv.__contains__("--graphics")
    log_to_file = sys.argv.__contains__("--logfile")
if run_with_graphics:
    print("Running simulations in graphics mode")
else:
    print("Running simulations in non-graphics mode")
if log_to_file:
    timestamp = datetime.datetime.now().__str__()
    timestamp = timestamp.replace(" ", "-")
    timestamp = timestamp[:-7]
    log_filename = "snake-eyes-%s.log" % timestamp
    print("Logs will be persisted to file: %s" % log_filename)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Running computations using %s" % device)
agent_head_only = HeadOnlyAgent(device=device)
agent_head_and_food = HeadAndFoodAgent(device=device)
agent_head_and_distance_to_food = HeadAndDistanceToFoodAgent(device=device)
game.set_run_with_graphics(run_with_graphics)
game.add_agent(agent_head_only)
game.add_agent(agent_head_and_food)
game.add_agent(agent_head_and_distance_to_food)
game.start_simulation()

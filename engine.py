import sys
import datetime
import game
import torch

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
game.start_simulation()
import random


snakes = []
free_snake_indices = []
snakes_alive = []


def init_snakes(p_snakes):
    global snakes
    global free_snake_indices
    global snakes_alive
    snakes = p_snakes
    free_snake_indices = list(range(0, len(snakes)))
    snakes_alive = [True] * len(snakes)


def available_snake():
    global snakes
    global free_snake_indices
    index = random.randint(0, len(free_snake_indices) - 1)
    ret_snake = snakes[free_snake_indices[index]]
    # print("Returning snake with indent %d" % free_snake_indices[index])
    del free_snake_indices[index]
    return ret_snake


def is_snake_alive(i):
    global snakes_alive
    return snakes_alive[i]


def kill_snake(i):
    global snakes_alive
    snakes_alive[i] = False


def reset_snake_life():
    global free_snake_indices
    free_snake_indices = list(range(0, len(snakes_alive)))
    for i in range(0, len(snakes)):
        snakes_alive[i] = True


def terminated():
    for i in range(0, len(snakes_alive)):
        if snakes_alive[i]:
            return False
    return True

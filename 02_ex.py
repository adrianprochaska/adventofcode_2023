import numpy as np


def parse_input(line):
    game_id, rest = line[5:].split(": ")
    game_id = int(game_id)
    rounds = rest[:-1].split("; ")
    game_array = np.zeros((3, len(rounds)))
    for idx_round, round in enumerate(rounds):
        colors = round.split(", ")
        for color in colors:
            n_cubes, str_color = color.split(" ")
            if str_color == "red":
                idx_color = 0
            elif str_color == "green":
                idx_color = 1
            elif str_color == "blue":
                idx_color = 2
            game_array[idx_color, idx_round] = int(n_cubes)

    return game_id, game_array


def check_possible(game_array):
    max_vals = np.amax(game_array, axis=1)
    power_of_cubes = int(max_vals.prod())
    if power_of_cubes == 0:
        print("Das Ergebnis war 0.")
    # print("Power: " + str(power_of_cubes))

    lim_vals = np.array([12, 13, 14]) - max_vals
    if np.amin(lim_vals) < 0:
        is_possible = False
    else:
        is_possible = True

    return is_possible, power_of_cubes


sum_possible = 0
sum_power = 0
with open("02_in.txt") as f:
    for line in f:
        game_id, game_array = parse_input(line)
        is_possible, power_of_cubes = check_possible(game_array)
        sum_power = sum_power + power_of_cubes
        if is_possible:
            sum_possible += game_id

print("Sum of possible: " + str(sum_possible))
print("Sum of powers: " + str(sum_power))

import numpy as np
import re
import copy

winning_points = 0

with open("04_in.txt") as f:
    for line in f:
        count_wins = 0
        only_numbers = line.split(": ")[1]
        winning_numbers, our_numbers = only_numbers.split(" | ")
        a_winning = list(map(int, winning_numbers.split()))
        a_ours = list(map(int, our_numbers.split()))

        for win in a_winning:
            if win in a_ours:
                count_wins += 1

        if count_wins > 0:
            winning_points += 2**(count_wins-1)

print("Winning points: " + str(winning_points))
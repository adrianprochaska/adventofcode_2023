import numpy as np
import re
import copy


str_file = []
with open("04_in.txt") as f:
    for line in f:
        str_file.append(line)

winning_cards = np.ones(len(str_file))
n_line = 0

for line in str_file:
    count_wins = 0
    only_numbers = line.split(": ")[1]
    winning_numbers, our_numbers = only_numbers.split(" | ")
    a_winning = list(map(int, winning_numbers.split()))
    a_ours = list(map(int, our_numbers.split()))

    factor = winning_cards[n_line]

    for win in a_winning:
        if win in a_ours:
            count_wins += 1
            winning_cards[n_line + count_wins] = winning_cards[n_line + count_wins] + factor

    n_line += 1

print("Number of cards: " + str(sum(winning_cards)))

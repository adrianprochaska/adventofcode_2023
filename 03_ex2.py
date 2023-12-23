import numpy as np
import re
import copy

special_characters = r"[\*]"

num_pattern = r"[0-9]+"

a_num = []
a_span = []
a_special = []
n_line = 0

with open("03_in.txt") as f:
    for line in f:
        num_loc = []
        span_loc = []
        for m in re.finditer(num_pattern, line):
            # get number
            num_loc.append(int(m.group()))
            # get index of every number
            span_loc.append(np.arange(m.start(), m.end()))

        # get index of every special character
        a_special.append([(m.start()) for m in re.finditer(special_characters, line)])

        a_num.append(num_loc)
        a_span.append(span_loc)

sum_gear = 0

n_line = 0
max_line = len(a_special) - 1
for line in a_special:
    for char_special in line:
        gear_count = 0
        gear_ratio = 1
        for n_line_loc in range(max(0, n_line - 1), min(max_line, n_line + 1) + 1):
            for idx_span, span_loc in reversed(list(enumerate(a_span[n_line_loc]))):
                do_pop = False
                for idx_col in range(char_special - 1, char_special + 2):
                    if idx_col in span_loc:
                        do_pop = True

                if do_pop:
                    gear_count += 1
                    gear_ratio *= a_num[n_line_loc][idx_span]
        if gear_count == 2:
            sum_gear += gear_ratio

    n_line += 1


print(sum_gear)
# print("".join(set(str_set)))
# print("Solution" + str(sum_possible))

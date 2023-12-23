import numpy as np
import re
import copy

special_characters = r"[\=\+\%\-\@\/\*\#\$\&]"

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

a_num_orig = copy.deepcopy(a_num)
n_line = 0
max_line = len(a_special) - 1
for line in a_special:
    for char_special in line:
        for n_line_loc in range(max(0, n_line - 1), min(max_line, n_line + 1) + 1):
            for idx_span, span_loc in reversed(list(enumerate(a_span[n_line_loc]))):
                do_pop = False
                for idx_col in range(char_special - 1, char_special + 2):
                    if idx_col in span_loc:
                        do_pop = True

                if do_pop:
                    a_num[n_line_loc].pop(idx_span)
                    a_span[n_line_loc].pop(idx_span)

    n_line += 1


sum_of_matching = sum([sum(x) for x in a_num_orig]) - sum([sum(x) for x in a_num])

print(sum_of_matching)
# print("".join(set(str_set)))
# print("Solution" + str(sum_possible))

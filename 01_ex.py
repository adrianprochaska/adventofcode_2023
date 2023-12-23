sum_of_numbers = 0
first_digit = 0
last_digit = 0

with open('01_in.txt') as f:
    for line in f:
        len_of_line = len(line)
        # find first digit´
        i = 0
        while i < len_of_line:
            if line[i].isdigit():
                first_digit = int(line[i])
                break
            i += 1
        else:
            print("something went wrong")

        i = len_of_line - 1
        # find last digit
        while i > -1:
            if line[i].isdigit():
                last_digit = int(line[i])
                break
            i-=1
        else:
            print("something went wrong")

        sum_of_numbers += 10*first_digit + last_digit


print("The sum is : " + str(sum_of_numbers))

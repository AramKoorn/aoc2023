import re


f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]


t = 0


# part 1
for l in lines:
    first_digit_pattern = r'\d'
    first_digit_match = re.search(first_digit_pattern, l)
    first_digit = first_digit_match.group()

    # Regular expression to find the last digit
    last_digit_pattern = r'(\d)(?!.*\d)'
    last_digit_match = re.search(last_digit_pattern, l)
    last_digit = last_digit_match.group(1)

    n = int(str(first_digit) + str(last_digit))
    t += n
print("part1 ", t)


# part two
ints = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
t = 0 
for idx, l in enumerate(lines):
    # print(idx)
    # FInd first digit
    d = {}
    d_r = {}
    for nm, numeric in ints.items():
        if nm in l:
            d[l.find(nm)] = numeric
            d_r[l.rfind(nm)] = numeric
    if len(d) > 0:
        i = sorted(list(d))
        first = i[0]
        last = sorted(list(d_r))[-1]

    first_digit_pattern = r'\d'
    first_digit_match = re.search(first_digit_pattern, l)
    first_digit = first_digit_match.group() if first_digit_match else None

    # Regular expression to find the last digit
    last_digit_pattern = r'(\d)(?!.*\d)'
    last_digit_match = re.search(last_digit_pattern, l)
    last_digit = last_digit_match.group(1) if last_digit_match else None

    if first_digit is None:
        n = int(str(d[first]) + str(d[last]))
        # print(n)
        t += n
        continue
    if len(d) == 0:
        n = int(str(first_digit) + str(last_digit))
        t += n
        continue
    else:
        if first_digit_match.span()[0] < first:
            f_f = first_digit
        else:
            f_f = d[first]

        if last_digit_match.span()[0] > last:
            f_l = last_digit
        else:
            f_l = d_r[last]

        n = int(str(f_f) + str(f_l))
        t += n
    d = True

print("part2 ", t)



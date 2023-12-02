import re
from functools import reduce

f = open("input.txt")
lines = f.readlines()

t = 0
for i, l in enumerate(lines):
    red, green, blue = 12, 13, 14
    sets = l.split(":")[1]
    sets = sets.split(";")
    pattern = r"(\d+)\s(\w+)"

    valid = True
    for s in sets:
        matches = re.findall(pattern, s)
        data = {color: int(number) for number, color in matches}
        for color, number in data.items():
            if number > eval(color):
                valid = False
                break
    if valid:
        t += (i + 1)
print("part1: ", t)

t = 0
for i, l in enumerate(lines):
    mx = {"red": 0, "green": 0, "blue": 0}
    sets = l.split(":")[1]
    sets = sets.split(";")
    pattern = r"(\d+)\s(\w+)"

    valid = True
    for s in sets:
        matches = re.findall(pattern, s)
        data = {color: int(number) for number, color in matches}
        for color, number in data.items():
            mx[color] = max(mx[color], number)

    product = reduce(lambda x, y: x * y, list(mx.values()))
    t += product
print("part2: ", t)







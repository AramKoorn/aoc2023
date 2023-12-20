from copy import deepcopy
from pprint import pprint


def mirrored(g):
    # Horizontal
    # pprint(g)
    for i in range(1, len(g)):
        mn = min(i, len(g) - i)
        l = g[i - mn:i]
        r = g[i:i + mn]

        if l == r[::-1]:
            return i
    return 0


f = open("input.txt")
lines = f.readlines()
lines = [l.strip("\n") for l in lines]
lines
patterns = []

grid = []
for line in lines:
    if line == "":
        patterns.append(deepcopy(grid))
        grid = []
        continue
    grid.append([x for x in line.strip("\n")])

patterns.append(grid)

t = 0
for p in patterns:

    # rows
    t += mirrored(p) * 100

    # Column split
    t += mirrored([list(reversed(col)) for col in zip(*p)])

print(t)

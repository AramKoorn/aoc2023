from collections import Counter
from copy import deepcopy
from pprint import pprint


f = open('input.txt', 'r')
lines = [l.strip("\n") for l in f.readlines()]
grid = [[x for x in l] for l in lines]

n = len(grid)
m = len(grid[0])


def slide(grid, direction=(-1, 0)):
    changes = 0
    steps = 0
    n = len(grid)
    m = len(grid[0])

    dx = direction[0]
    dy = direction[1]

    while changes != 0 or steps == 0:
        changes = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "O":
                    if 0 <= i + dx < n and 0 <= j + dy < m:
                        if grid[i + dx][j + dy] == ".":
                            grid[i + dx][j + dy] = "O"
                            grid[i][j] = "."
                            changes += 1
        steps += 1
    return grid


cycles = ((-1, 0), (0, -1), (1, 0), (0, 1))


def get_load(grid):
    t = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "O":
                t += abs(i - (n))
    return t


def find_cycle_length():

    cnt = 0
    tmp = deepcopy(grid)
    c = Counter()
    mx = 0
    iters = []
    lookup = {}

    while 3 not in c.values():

        for dir in cycles:
            tmp = slide(deepcopy(tmp), dir)
        cnt += 1
        c[''.join(map(str, [item for sublist in tmp for item in sublist]))] += 1
        lookup[cnt] = get_load(tmp)
        if max(mx, max(c.values())) > mx:
            mx = max(mx, max(c.values()))
            iters.append(cnt)
    return iters, lookup


cnts, lookup = find_cycle_length()
cycle = (cnts[-1] - cnts[-2])
print(lookup[(cnts[1] - 1) + ((1000000000 - (cnts[1] - cnts[0])) % cycle)])

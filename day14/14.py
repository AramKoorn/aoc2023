from collections import defaultdict
from copy import deepcopy


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


grid = slide(deepcopy(grid))

t = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "O":
            t += abs(i - (n))

print(t)

f = open("input.txt", "r")
lines = f.readlines()
lines = [l.split("\n") for l in lines]

SCALE = 1

grid = []
for x in lines:
    grid.append([x for x in x[0]])

n = len(grid)
m = len(grid[0])

cords = []
rows = []
cols = []

for i in range(n):
    cnt = 0
    for j in range(m):
        if grid[i][j] != ".":
            cnt += 1
        if grid[i][j] == "#":
            cords.append((i, j))
    if cnt == 0:
        rows.append(i)

for col in range(m):
    cnt = 0
    for row in range(n):
        if grid[row][col] == "#":
            cnt += 1
    if cnt == 0:
        cols.append(col)

rows = rows[::-1]
cols = cols[::-1]

for row in rows:
    new_cords = []
    for x, y in cords:
        if x > row:
            new_cords.append((x + SCALE, y))
        else:
            new_cords.append((x, y))
    cords = new_cords
print(cords)

for col in cols:
    new_cords = []
    for x, y in cords:
        if y > col:
            new_cords.append((x, y + SCALE))
        else:
            new_cords.append((x, y))
    cords = new_cords


from itertools import combinations
combs = combinations(cords, 2)
t = 0
for (x1, y1), (x2, y2) in combs:
    t += abs(x1 - x2) + abs(y1 - y2)
print(t)





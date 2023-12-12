f = open("input.txt", "r")
lines = f.readlines()
lines = [l.split("\n") for l in lines]

grid = []
for x in lines:
    grid.append([x for x in x[0]])

n = len(grid)
m = len(grid[0])

start = None
for i in range(n):
    for j in range(m):
        if start is None:
            if grid[i][j] == "S":
                start = (i, j)

expand_mapping = {
'|': ".|.\n.|.\n.|.",
'-': "...\n---\n...",
'L': ".|.\n.L-\n...",
'J': ".|.\n-J.\n...",
'7': "...\n-7.\n.|.",
'F':"...\n.F-\n.|.",
'.': "...\n...\n...",
}

def create_expanded_grid(og, pipes):

    for i in range(len(og)):
        for j in range(len(og[0])):
            if (i, j) not in pipes:
                og[i][j] = "."

    # Define the mapping
    expanded_grid = []
    for l in og:
        r1, r2, r3 = [], [], []
        for char in "".join(l):
            splitted = expand_mapping[char.replace("S", "F")].split("\n")
            r1.extend(splitted[0])
            r2.extend(splitted[1])
            r3.extend(splitted[2])
        expanded_grid.append(r1)
        expanded_grid.append(r2)
        expanded_grid.append(r3)

    return expanded_grid



# BFS
directions = {
    "|": ((1, 0), (-1, 0)),  # Norh and south
    "-": ((0, 1), (0, -1)),  # west and east
    "L": ((-1, 0), (0, 1)),  # north and east
    "J": ((-1, 0), (0, -1)),  # North and west
    "7": ((1, 0), (0, -1)),  # South and west
    "F": ((1, 0), (0, 1)),  # south and east
    "S": ((1, 0), (0, 1), (-1, 0), (0, -1))
}

allowed = {
    (1, 0): ["|", "L", "J"],  # Going down
    (-1, 0): ["|", "7", "F"],  # going up
    (0, -1): ["-", "L", "F"],  # Going west
    (0, 1): ["-", "J", "7"]  # Going east
}
print(start)


def bfs(start, pipe):

    if pipe is not None:
        grid[start[0]][start[1]] = pipe

    visited = set()  # Set to keep track of visited nodes.
    q = []  # Initialize a queue
    q.append(start)
    visited.add(start)

    while q:
        node = q.pop(0)
        x, y = node
        for dx, dy in directions[grid[x][y]]:
            i = x + dx
            j = y + dy
            if 0 <= i < n and 0 <= j < m and (i, j) != (x, y):
                if (i, j) not in visited and grid[i][j] in allowed[(dx, dy)]:
                    q.append((i, j))
                    visited.add((i, j))
    return visited

pipes = bfs(start, pipe="F")

from copy import deepcopy
expanded_grid = create_expanded_grid(deepcopy(grid), pipes)

grid = []
for i in range(n):
    row = []
    for j in range(m):
        if (i, j) in pipes:
            row.append("x")
        else:
            row.append(" ")
    grid.append(row)
    print(row)


def bfs2(start):

    seen = set()
    q = [start]
    seen.add(start)
    batch = set()
    spillage = False

    while q:
        x, y = q.pop(0)
        batch.add((x, y))
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            spillage = True
        grid[x][y] = "w"
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            i = x + dx
            j = y + dy
            if 0 <= i < n and 0 <= j < m and (i, j) not in seen:
                if grid[i][j] != "x":
                    q.append((i, j))
                    seen.add((i, j))
    if spillage:
        for x, y in batch:
            grid[x][y] = "O"

seen = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == " ":
            bfs2((i, j))
            d = True

def bfs3(start):

    seen = set()
    q = [start]
    seen.add(start)
    batch = set()
    spillage = False
    n = len(expanded_grid)
    m = len(expanded_grid[1])

    while q:
        x, y = q.pop(0)
        batch.add((x, y))
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            spillage = True
        expanded_grid[x][y] = "w"
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            i = x + dx
            j = y + dy
            if 0 <= i < n and 0 <= j < m and (i, j) not in seen:
                if expanded_grid[i][j] not in list(directions):
                    q.append((i, j))
                    seen.add((i, j))
    if spillage:
        for x, y in batch:
            expanded_grid[x][y] = "O"


seen = set()
for i in range(len(expanded_grid)):
    for j in range(len(expanded_grid[0])):
        if expanded_grid[i][j] == ".":
            bfs3((i, j))
            d = True

for r in expanded_grid:
    print(r)

t = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "w":
            print(expanded_grid[(i * 3) + 1][(j * 3) + 1])
            if expanded_grid[(i * 3) + 1][(j * 3) + 1] == "w":
                t += 1
print(t)

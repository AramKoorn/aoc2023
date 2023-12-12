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

visited = bfs(start, pipe="F")
print(len(visited) // 2)

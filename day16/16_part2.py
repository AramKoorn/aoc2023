from pprint import pprint

f = open("input.txt")
grid = [[x for x in l.strip("\n")] for l in f.readlines()]
# pprint(grid)

n = len(grid)
m = len(grid[0])


def energize(start):

    visited = set()
    # visited.add(start)
    q = []
    q.append(start)

    while q:
        cords, dir = q.pop(0)
        x, y = cords
        dx, dy = dir
        if 0 <= x + dx < n and 0 <= y + dy < m:
            i = x + dx
            j = y + dy
            match grid[x + dx][y + dy]:
                case ".":
                    if ((i, j), dir) not in visited:
                        visited.add(((i, j), dir))
                        q.append(((i, j), dir))
                case "|":
                    if dir == (1, 0) or dir == (-1, 0):
                        if ((i, j), dir) not in visited:
                            visited.add(((i, j), dir))
                            q.append(((i, j), dir))
                    else:
                        if ((i, j), (1, 0)) not in visited:
                            visited.add(((i, j), (1, 0)))
                            q.append(((i, j), (1, 0)))
                        if ((i, j), (-1, 0)) not in visited:
                            visited.add(((i, j), (-1, 0)))
                            q.append(((i, j), (-1, 0)))
                case "-":
                    if dir == (0, -1) or dir == (0, 1):
                        if ((i, j), dir) not in visited:
                            visited.add(((i, j), dir))
                            q.append(((i, j), dir))
                    else:
                        if ((i, j), (0, 1)) not in visited:
                            visited.add(((i, j), (0, 1)))
                            q.append(((i, j), (0, 1)))
                        if ((i, j), (0, -1)) not in visited:
                            visited.add(((i, j), (0, -1)))
                            q.append(((i, j), (0, -1)))
                case "/":
                    if dir == (0, -1):
                        if ((i, j), (1, 0)) not in visited:
                            visited.add(((i, j), (1, 0)))
                            q.append(((i, j), (1, 0)))
                    if dir == (0, 1):
                        if ((i, j), (-1, 0)) not in visited:
                            visited.add(((i, j), (-1, 0)))
                            q.append(((i, j), (-1, 0)))
                    if dir == (1, 0):
                        if ((i, j), (0, -1)) not in visited:
                            visited.add(((i, j), (0, -1)))
                            q.append(((i, j), (0, -1)))
                    if dir == (-1, 0):
                        if ((i, j), (0, 1)) not in visited:
                            visited.add(((i, j), (0, 1)))
                            q.append(((i, j), (0, 1)))
                case "\\":
                    if dir == (0, -1):
                        if ((i, j), (-1, 0)) not in visited:
                            visited.add(((i, j), (-1, 0)))
                            q.append(((i, j), (-1, 0)))
                    if dir == (0, 1):
                        if ((i, j), (1, 0)) not in visited:
                            visited.add(((i, j), (1, 0)))
                            q.append(((i, j), (1, 0)))
                    if dir == (1, 0):
                        if ((i, j), (0, 1)) not in visited:
                            visited.add(((i, j), (0, 1)))
                            q.append(((i, j), (0, 1)))
                    if dir == (-1, 0):
                        if ((i, j), (0, -1)) not in visited:
                            visited.add(((i, j), (0, -1)))
                            q.append(((i, j), (0, -1)))

    # print(len(visited))
    cells = set()
    for cords, _ in visited:
        cells.add(cords)
    return len(cells)


start = ((0, -1), (0, 1))
e = energize(start)
mx = 0
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

for x, y in [(x, -1) for x in range(n)] + [(x, m) for x in range(n)] + [(-1, x) for x in range(m)] + [(n, x) for x in range(m)]:
    for dir in dirs:
        mx = max(mx, energize(((x, y), dir)))

print(mx)

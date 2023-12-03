f = open("input.txt", "r")
lines = f.readlines()
lines = [l.split("\n") for l in lines]

grid = []
for x in lines:
    grid.append([x for x in x[0]])

n = len(grid)
m = len(grid[0])


def check_part(i, j, skip):
    offset = ((1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
    for dx, dy in offset:
        if 0 <= dx + i < n and 0 <= j + dy < m and (i + dx, j + dy) not in skip:
            if grid[i + dx][j + dy] != ".":
                return True
    return False


numbers = []
seen = set()

t = 0
for i in range(n):
    for j in range(m):
        if (i, j) not in seen:
            integer = []
            cords = []
            if grid[i][j].isnumeric():
                # Get the number
                while grid[i][j].isnumeric() and j < m:
                    seen.add((i, j))
                    cords.append((i, j))
                    integer.append(grid[i][j])
                    j += 1
                    if j >= m:
                        break
                numbers.append((int("".join(integer)), cords))

t = 0
for nm, cords in numbers:
    for i, j in cords:
        if check_part(i, j, cords):
            t += nm
            break
print("part1: ", t)

# Part 2:
number_map = {}
for nm, cords in numbers:
    for i, j in cords:
        number_map[(i, j)] = nm

t = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "*":
            seen = set()
            cnt = 0
            gears = []
            offset = ((1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
            for dx, dy in offset:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m and (x, y) not in seen:
                    if (x, y) in number_map:
                        gears.append(number_map[(x, y)])
                        # Get all indices for that number
                        for _, crds in numbers:
                            if (x, y) in crds:
                                seen.update(crds)
                                break
            if len(gears) == 2:
                t += (gears[0] * gears[1])
print("part2: ", t)

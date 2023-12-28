from heapq import heappush, heappop

f = open("input.txt")
grid = [list(map(int, line.strip())) for line in f]

n = len(grid)
m = len(grid[0])

cnt = 0
q = [(0, (0, 0), (0, 0), cnt)]
visited = set()
offset = ((1, 0), (0, 1), (-1, 0), (0, -1))

while q:
    t, cords, prev, cnt = heappop(q)

    if (cords, prev, cnt) in visited:
        continue

    visited.add((cords, prev, cnt))

    # Reached the end
    if cords == (n - 1, m - 1) and cnt >= 4:
        print(t)
        break

    if cnt < 10 and prev != (0, 0):
        x, y = cords[0] + prev[0], cords[1] + prev[1]
        if 0 <= x < n and 0 <= y < m:
            heappush(q, (t + grid[x][y], (x, y), prev, cnt + 1))

    if cnt >= 4 or prev == (0, 0):
        for dx, dy in offset:
            # Check not equal than prev and should be 90 degree rotation
            if (dx, dy) != prev and (dx, dy) != (-prev[0], -prev[1]):
                x, y = cords[0] + dx, cords[1] + dy
                if 0 <= x < n and 0 <= y < m:
                    heappush(q, (t + grid[x][y], (x, y), (dx, dy), 1))

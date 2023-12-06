import re

f = open("input.txt", "r")
lines = f.readlines()
times, distances = [list(map(int, re.findall(r'\d+', x.strip('\n')))) for x in lines]

tot = 1
for i, t in enumerate(times):
    start = t
    cnt = 0
    while start != 0:
        left = abs(start - t)
        dist = left * start
        if dist > distances[i]:
            cnt += 1
        start -= 1
    tot *= cnt
print("part1: ", tot)

# Part 2
time = int("".join([str(x) for x in times]))
distance = int("".join([str(x) for x in distances]))

for i in range(time):

    left = abs(i - time)
    dist = left * i
    if dist > distance:
        break

print("part2: ", (time - (i * 2) + 1))

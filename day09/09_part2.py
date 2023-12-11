import re


f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
lines = [list(map(int, re.findall(r'-?\d+', x))) for x in lines]


def diffs(arr):
    d = []
    for i in range(1, len(arr)):
        d.append(arr[i] - arr[i - 1])
    return d

t = 0
for l in lines:
    l = l[::-1]
    last = []
    diff = diffs(l)
    last.append(diff[-1])
    while not all(x == 0 for x in diff):
        diff = diffs(diff)
        last.append(diff[-1])
    debug = True
    t += sum(last) + l[-1]

print(t)





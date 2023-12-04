import re
from collections import defaultdict, Counter


f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]


def points(n):
    res = 0
    for i in range(n):
        if i == 0:
            res = 1
        else:
            res *= 2
    return res


t = 0
winning = defaultdict(int)
c = Counter()

for i, l in enumerate(lines):
    splitted = l.split("Card ")[1].split(":")[1].split("|")
    left = [int(number) for number in re.findall(r'\d+', splitted[0])]
    right = [int(number) for number in re.findall(r'\d+', splitted[1])]
    t += points(len(set(left) & set(right)))
    winning[i + 1] = len(set(left) & set(right))
    c[i + 1] = 1
print("part1 ", t)


cards = list(c)
for card in cards:
    win = winning[card]
    repeat = c[card]
    for i in range(card + 1, card + win + 1):
        c[i] += 1 * repeat

t = 0
for card in cards:
    t += c[card]
print("part2 ", t)

from math import lcm


f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]
mappings = {}
for i, l in enumerate(lines):
    if i == 0:
        ins = l
        continue
    else:
        splitted = l.split("=")
    if len(splitted) == 2:
        mappings[splitted[0].strip()] = (
            splitted[1].strip().split(",")[0].replace("(", ""),
            splitted[1].replace(" ", "").split(",")[1].replace(")", ""))

curr = [x for x in list(mappings) if x[2] == "A"]


def find_cycle(node):
    i = 0
    while not node.endswith('Z'):
        d = ins[i % len(ins)]
        node = mappings[node][0 if d == 'L' else 1]
        i += 1
    return i


cycles = [find_cycle(c) for c in curr]

lm = 1
for s in cycles:
    lm = lcm(lm, s)
print(lm)

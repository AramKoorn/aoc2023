import re
from collections import defaultdict
from tqdm import tqdm


f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

mappings = defaultdict(list)
for i, l in enumerate(lines):
    if i == 0:
        seeds = list(map(int, re.findall(r'\d+', l)))
        continue

    if len(l.split("-")) == 3:
        key = (l.split("-")[0], l.split("-")[2].replace(" map:", ""))
        mappings[key]
        continue

    if l != "":
        mappings[key].append(list(map(int, re.findall(r'\d+', l))))


ends = set()

# part 2 (brute-force in reverse)
# OPTIMIZE LATER
d = True
for s in seeds:
    start = "seed"
    while start != "location":
        # Get key
        for k in list(mappings):
            if k[0] == start:
                mp = mappings[k]
                break

        for dest, source, rng in mp:
            if source <= s < source + rng:
                dist = abs(s - source)
                s = dest + dist
                break
        start = k[1]
    # print(s)
    ends.add(s)

print(min(ends))
ans = min(ends)

seed_ranges = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
ok = True
s = 0
for s in tqdm(range(ans)):
    if not ok:
        break
    org = s
    start = "location"
    while start != "seed":
        # Get key
        for k in list(mappings):
            if k[1] == start:
                mp = mappings[k]
                break

        for dest, source, rng in mp:
            if dest <= s < dest + rng:
                s = source + abs(s - dest)
                break
        start = k[0]

    for l, r in seed_ranges:
        if l <= s < l + r:
            print("answer: ", org)
            ok = False
    s = org + 1


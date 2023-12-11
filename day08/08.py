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
        splitted[1].strip().split(",")[0].replace("(", ""), splitted[1].replace(" ", "").split(",")[1].replace(")", ""))
curr = "AAA"
i = 0
while curr != "ZZZ":
    d = ins[i % len(ins)]
    mp = mappings[curr]
    if d == "L":
        curr = mp[0]
    else:
        curr = mp[1]
    i += 1

print(i)



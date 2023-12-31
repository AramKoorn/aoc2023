import re
from copy import deepcopy


f = open("input.txt")

def flow(vars, curr="in"):
    # print(vars)

    if curr == "A":
        prod = 1
        for v in vars.values():
            prod *= v[1] - v[0] + 1
        return prod
    if curr == "R":
        return 0

    t = 0
    statements = rules[curr]

    for st in statements:
        print(st)

        if "<" not in st and ">" not in st:
            print(st)
            t += flow(vars, st)
            break
        if "<" in st:
            ch, splitted = st.split("<")
            n, nw = splitted.split(":")
            n = int(n)
            left = min(vars[ch][0], n)
            right = min(vars[ch][1], n - 1)
            T = (left, right)  # True
            F = (right + 1, vars[ch][1])  # False
        else:
            ch, splitted = st.split(">")
            n, nw = splitted.split(":")
            n = int(n)
            left = max(vars[ch][0], n + 1)
            T = (left, vars[ch][1])
            F = (vars[ch][0], left - 1)

        # Trigger True condition
        copy = deepcopy(vars)
        copy[ch] = T
        t += flow(copy, nw)

        # Update ranges when False
        vars = deepcopy(vars)
        vars[ch] = F
    return t

rules = {}
rl = True
t = 0
for l in f.readlines():
    if l == "\n":
        rl = False
        continue
    if rl:
        l = l.strip()
        k = l.split("{")[0]
        patten = "\{([^}]*)\}"
        r = re.findall(patten, l)[0].split(",")
        rules[k] = r

print(rules)
print(flow({key: (1, 4000) for key in "xmas"}))

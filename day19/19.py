import re

f = open("input.txt")

def flow(vars, curr="in"):

    if curr == "A":
        return True
    if curr == "R":
        return False

    x = vars["x"]
    m = vars["m"]
    a = vars["a"]
    s = vars["s"]

    # start with in
    statements = rules[curr]

    for st in statements:
        if ":" in st:
            if eval(st.split(":")[0]):
                return flow(vars, st.split(":")[1])
        else:
            return flow(vars, st)


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
    else:
        patten = "\{([^}]*)\}"
        r = re.findall(patten, l)[0].split(",")
        vr = {}
        for var in r:
            splited = var.split("=")
            vr[splited[0]] = int(splited[1])

        if flow(vr):
            t += sum(vr.values())
print(t)

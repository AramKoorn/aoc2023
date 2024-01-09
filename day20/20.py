f_targets = lambda x: [x.strip()] if "," not in x else [x.strip() for x in x.split(",")]

class Module:
    def __init__(self, state, name, targets, type) :
        self.state = state
        self.name = name
        self.targets = targets
        self.type = type

        if self.type == "&":
            self.memory = {}

    def __repr__(self):
        return self.name

f = open("input.txt")

modules = {}

for l in f.readlines():
    # pprint(l.strip("\n"))

    splitted = l.strip().split(" -> ")
    match splitted[0][0]:
        case "%":
            m = Module(state=0, name=splitted[0][1:], targets=f_targets(splitted[1]), type="%")
        case "&":
            m = Module(state="lo", name=splitted[0][1:], targets=f_targets(splitted[1]), type="&")
        case "b":
            m = Module(state="lo", name=splitted[0], targets=f_targets(splitted[1]), type="broadcaster")
    modules[str(m)] = m

# Init memory
for name, module in modules.items():
    for output in module.targets:
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = "lo"

flip_signal = lambda signal: "lo" if signal == "hi" else "hi"

modules["output"] = Module(state="lo", name="output", type="out", targets=[])
modules["rx"] = Module(state=0, name="rx", type="out", targets=[])

def cycle(q):

    cnt_low = 0
    cnt_high = 0
    while q:
        mod, signal = q.pop(0)
        if str(mod) == "jl":
            debug = True
        if signal == "hi":
            cnt_high += 1
        else:
            cnt_low += 1

        match mod.type:
            case "broadcaster":
                for t in mod.targets:
                    q.append((modules[t], signal))
            case "start":
                for t in mod.targets:
                    q.append((modules[t], signal))
            case "%":
                if signal == "lo":
                    mod.state = abs(mod.state - 1)
                    # print(mod.state)
                    if mod.state == 1:
                        signal = "hi"
                    else:
                        signal = "lo"
                    for t in mod.targets:
                        if modules[t].type == "&":
                            modules[t].memory[str(mod)] = signal
                        q.append((modules[t], signal))
            case "&":
                if all([x == "hi" for x in mod.memory.values()]):
                    signal = "lo"
                else:
                    signal = "hi"
                for t in mod.targets:
                    if modules[t].type == "&":
                        modules[t].memory[str(mod)] = signal
                    q.append((modules[t], signal))
    return cnt_low, cnt_high


t_l, t_h = 0, 0
for _ in range(1000):
    l, h = cycle([(modules["broadcaster"], "lo")])
    # l, h = cycle([(Module(name="button", state=0, targets=["broadcaster"], type="start"), "lo")])
    # print(l, h)
    # print("---------------------------------")
    t_l += l
    t_h += h

print(t_l, t_h)
print(t_h * t_l)


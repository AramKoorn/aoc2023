f = open("input.txt")
ins = [x.strip() for x in f.readlines()]
cords = []

x = 0
y = 0
border = 0

for i in ins:
    d, step, hx = i.split(" ")
    step = int(step)
    border += step
    match d:
        case "R":
            y += step
        case "L":
            y -= step
        case "U":
            x -= step
        case "D":
            x += step
    cords.append((x, y))

area = 0.5 * abs(sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(cords, cords[1:] + cords[:1])))
inside = area - border // 2 + 1
print(int(inside + border))




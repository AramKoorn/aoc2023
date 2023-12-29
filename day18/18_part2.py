f = open("input.txt")
ins = [x.strip() for x in f.readlines()]
cords = []

x = 0
y = 0
border = 0

for i in ins:
    _, _, hx = i.split(" ")
    hx = hx[2:-1]
    step = int(hx[:5], 16)
    border += step
    d = hx[-1]
    match d:
        case "0":
            y += step
        case "2":
            y -= step
        case "3":
            x -= step
        case "1":
            x += step
    cords.append((x, y))

area = 0.5 * abs(sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(cords, cords[1:] + cords[:1])))
inside = area - border // 2 + 1
print(int(inside + border))




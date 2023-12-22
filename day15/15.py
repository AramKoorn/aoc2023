f = open("input.txt", "r")
chars = f.read().split(",")

t = 0
for s in chars:
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr %= 256
    t += curr

print(t)



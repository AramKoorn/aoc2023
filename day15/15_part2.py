f = open("input.txt", "r")
chars = f.read().split(",")

def hash(s):
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr


focals = {}
boxes = [[] for _ in range(256)]
for ins in chars:
    if "-" in ins:
        label = ins.split("-")[0]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        splitted = ins.split("=")
        label, focal = splitted[0], int(splitted[1])
        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)
        focals[label] = focal

t = 0
for i, box in enumerate(boxes):
    for j, label in enumerate(box):
        t += (i + 1) * (j + 1) * focals[label]
print(t)









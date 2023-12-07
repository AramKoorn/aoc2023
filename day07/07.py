from collections import Counter


f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(" ") for x in lines]
cards = [(c[0], int(c[1])) for c in lines]

bids = []
for hand, bid in cards:
    c = Counter(hand)
    score = sum([x ** 2 for x in c.values()])
    ranking = '23456789TJQKA'
    f_score = format(score, "02") + "".join([format(ranking.find(x), "02") for x in hand])
    bids.append((f_score, bid))

scores = sorted(bids, key= lambda x : x[0])
print(sum([(i + 1) * bid for i, (_, bid) in enumerate(scores)]))



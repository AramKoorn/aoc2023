from collections import Counter


f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip('\n').split(" ") for x in lines]
cards = [(c[0], int(c[1])) for c in lines]

bids = []
for hand, bid in cards:
    # Maximize score
    ranking = 'J23456789TQKA'
    tmp_scores = []
    for x in ranking:
        tmp = hand.replace("J", x)
        c = Counter(tmp)
        score = sum([x ** 2 for x in c.values()])
        f_score = format(score, "02") + "".join([format(ranking.find(x), "02") for x in hand])
        tmp_scores.append((f_score, tmp))
    winning = sorted(tmp_scores, key=lambda x : x[0])[-1]
    bids.append((winning[0], bid))

scores = sorted(bids, key= lambda x : x[0])
print(sum([(i + 1) * bid for i, (_, bid) in enumerate(scores)]))

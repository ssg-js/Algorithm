# 카드1
# 1313

n = int(input())

cards = [i for i in range(1, n+1)]

discarded = []
while True:
    discarded.append(cards.pop(0))
    if not cards:
        break
    a = cards.pop(0)
    cards.append(a)

print(*discarded)
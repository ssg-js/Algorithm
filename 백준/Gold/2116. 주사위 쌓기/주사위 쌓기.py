#  주사위 쌓기

n = int(input())

dices = [list(map(int, input().split())) for _ in range(n)]
first_dice = dices.pop(0)
match = [5, 3, 4, 1, 2, 0]

max_value = []
for i in range(6):
    total = 0
    clone = first_dice[:]
    top = clone[i]
    clone[i], clone[match[i]] = 0, 0
    total += max(clone)
    for dice in dices:
        for j, v in enumerate(dice):
            if v == top:
                clone = dice[:]
                top = clone[match[j]]
                clone[j], clone[match[j]] = 0, 0
                total += max(clone)
                break
    max_value.append(total)
print(max(max_value))

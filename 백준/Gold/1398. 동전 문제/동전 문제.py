import sys
from collections import defaultdict
read = sys.stdin.readline

firstCoins = []
secondCoins = []
firstExponent = 0
secondExponent = 0
while 10**firstExponent <= 10**15:
    firstCoins.append(10**firstExponent)
    firstExponent += 1
firstCoins.sort(reverse=True)
while 25*(100**secondExponent) <= 10**15:
    secondCoins.append(25*(100**secondExponent))
    secondExponent += 1
secondCoins.sort(reverse=True)

visited = defaultdict(int)
for coin in firstCoins:
    visited[coin] = 1
for coin in secondCoins:
    visited[coin] = 1

def recur(k):
    if visited[k]: return visited[k]
    case1, case2 = 10**15, 10**15

    for coin in secondCoins:
        if coin <= k:
            if visited[k-coin]: 
                case1 = visited[k-coin] + 1
                break
            case1 = recur(k-coin) + 1
            break
    for coin in firstCoins:
        if coin <= k:
            if visited[k-coin]: 
                case2 = visited[k-coin] + 1
                break
            case2 = recur(k-coin) + 1
            break
    
    visited[k] = min(case1, case2)
    return visited[k]

for _ in range(int(read())):
    k = int(read())
    if visited[k]: 
        print(visited[k])
        continue
    recur(k)
    print(visited[k])

    
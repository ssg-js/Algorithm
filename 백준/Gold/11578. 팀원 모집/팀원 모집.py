import sys
from itertools import combinations
read = sys.stdin.readline
n, m = map(int, read().split())
info = []
target = 2**n - 1
ans = -1
for _ in range(m):
    a, *arr = map(int, read().split())
    info.append(arr)
for i in range(1, m+1):
    for combi in combinations(info, i):
        bit = 0
        for person in combi:
            for elem in person:
                bit |= (1<<(elem-1))
        if bit == target:
            ans = i
            break
    if ans > 0:
        break
print(ans)
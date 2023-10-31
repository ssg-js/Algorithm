# [BOJ] 10836. 여왕벌
# 소요 시간 : 60분

import sys

size, days = map(int, sys.stdin.readline().split())
plus = [1] * (2 * size - 1)

for d in range(days):
    zero, one, two = map(int, sys.stdin.readline().split())
    for o in range(zero, zero + one):
        plus[o] += 1
    for t in range(zero + one, 2 * size - 1):
        plus[t] += 2

temp = plus[size:]
for i in range(size - 1, -1, -1):
    print(plus[i], *temp)

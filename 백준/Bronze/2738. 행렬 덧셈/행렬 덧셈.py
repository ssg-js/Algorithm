import sys
n, m = map(int, sys.stdin.readline().split())
first = []
second = []
for i in range(n):
    first.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    second.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    print(*map(lambda x: x[0] + x[1], zip(first[i],second[i])))
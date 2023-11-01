import sys
N = int(sys.stdin.readline())
have = dict()
for v in map(int, sys.stdin.readline().split()):
    have[v] = 1
M = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
ans = []
for v in data:
    if have.get(v):
        ans.append(1)
    else:
        ans.append(0)
print(*ans)
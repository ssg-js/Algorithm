import sys
baskets, commands = map(int, sys.stdin.readline().split())
ans = [0] * baskets
for _ in range(commands):
    s, e, n = map(int, sys.stdin.readline().split())
    ans[s-1:e] = [n]*(e-s+1)
print(*ans)
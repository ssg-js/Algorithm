import sys
n, m = map(int, sys.stdin.readline().split())
ans = [i for i in range(1, n + 1)]
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    for idx in range((e-s)//2 + 1):
        ans[s-1+idx], ans[e-1-idx] = ans[e-1-idx], ans[s-1+idx]
print(*ans)
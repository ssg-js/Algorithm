import sys

a, b = map(int, sys.stdin.readline().split())
ans = [(a + b) // 2, (a - b) // 2]
ans.sort(reverse=True)
if a < b:
    print(-1)
elif ans[0] + ans[1] == a and ans[0] - ans[1] == b:
    print(*ans)
else:
    print(-1)

import sys
ans = dict()
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n in ans:
        ans[n] += 1
    else:
        ans[n] = 1
ans = sorted(ans.items())
for v, n in ans:
    for _ in range(n):
        print(v)
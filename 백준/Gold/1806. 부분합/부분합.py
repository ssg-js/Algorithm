import sys
read = sys.stdin.readline

n, s = map(int, read().split())
arr = list(map(int, read().split()))
INF = 100001

ans = INF
l, r = 0, 0
value = arr[l]
while l <= r and r < n:
    if ans == 1:
        break
    if value < s:
        r += 1
        if r < n:
            value += arr[r]
    else:
        ans = min(ans, r-l+1)
        value -= arr[l]
        l += 1
        if r < l:
            r = l
if ans == INF:
    print(0)
else:
    print(ans)
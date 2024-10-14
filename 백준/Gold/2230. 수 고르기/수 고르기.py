import sys
read = sys.stdin.readline

n, m = map(int, read().split())
arr = []
for _ in range(n):
    arr.append(int(read()))
arr.sort()

l, r = 0, 0
ans = 2000000001
while l <= r:
    if ans == m:
        break
    if r == n:
        break
    elif l == r:
        r += 1
    elif arr[r] - arr[l] < m:
        r += 1
    else:
        ans = min(ans, arr[r]-arr[l])
        l += 1
print(ans)
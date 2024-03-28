import sys
read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))
arr.sort()
target_v = int(read())
start, end = 0, n-1
ans = 0
while start < end:
    if arr[start] + arr[end] > target_v:
        end -= 1
        continue
    if arr[start] + arr[end] < target_v:
        start += 1
        continue
    ans += 1
    start += 1
    end -= 1
print(ans)

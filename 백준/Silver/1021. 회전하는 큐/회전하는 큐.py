import sys

read = sys.stdin.readline

n, m = map(int, read().split())
arr = [i + 1 for i in range(n)]
ans = 0
now = 0
nums = list(map(int, read().split()))
for num in nums:
    move = 0
    while move < len(arr):
        left = now - move
        if left < 0:
            left = len(arr) + left
        right = (now + move) % len(arr)

        if arr[right] == num:
            now = right
            break
        if arr[left] == num:
            now = left
            break

        move += 1
    ans += move
    del arr[now]
    if len(arr) > 0:
        now = now % len(arr)
print(ans)
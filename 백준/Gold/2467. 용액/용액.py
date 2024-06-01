import sys
read = sys.stdin.readline
n = int(read())
arr = [*map(int, read().split())]
left, right = 0, n-1
compare = 2000000000
ans = []
while left < right:
    value = arr[left] + arr[right]
    if value == 0:
        ans = [arr[left], arr[right]]
        break
    if abs(value) < compare:
        compare = abs(value)
        ans = [arr[left], arr[right]]
    if value > 0:
        right -= 1
    else:
        left += 1
print(*ans)
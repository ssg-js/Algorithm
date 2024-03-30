import sys
read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))
arr.sort()
s, e = 0, n-1 # idx
value = 9876543210
ans = []
while s < e:
    mixture = arr[s]+arr[e]
    if abs(mixture) < value:
        value = abs(mixture)
        ans = [arr[s], arr[e]]
        if value == 0:
            break
    # 0이랑 비교해서 s, e 조절
    if mixture < 0:
        s += 1
    elif mixture > 0:
        e -= 1
print(*ans)
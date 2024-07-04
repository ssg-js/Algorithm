import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = []


def bi_trans(x):
    ret = [1]
    num = 1
    x -= num
    while x > 0:
        tmp = x
        num *= 2
        x -= num
        if x < 0:
            ret.append(tmp)
        else:
            ret.append(num)
    return ret


for _ in range(n):
    v, c, k = map(int, read().split())
    for i in bi_trans(k):
        arr.append((i*v, i*c))
l = len(arr)
dp = [[0] * (m+1) for _ in range(2)]

for i in range(1, l+1):
    idx = i % 2
    weight, value = arr[i-1]
    for j in range(m+1):
        before_line = (idx+1) % 2
        if weight > j:
            dp[idx][j] = dp[before_line][j]
        else:
            rest = j-weight
            if dp[before_line][rest] + value > dp[before_line][j]:
                dp[idx][j] = dp[before_line][rest] + value
            else:
                dp[idx][j] = dp[before_line][j]

print(dp[l % 2][-1])

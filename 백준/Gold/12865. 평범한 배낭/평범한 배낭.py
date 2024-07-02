import sys
read = sys.stdin.readline
n, k = map(int, read().split())
arr = [tuple(map(int, read().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    idx = i-1
    weight = arr[idx][0]
    value = arr[idx][1]
    for j in range(k+1):
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            rest = j-weight
            if dp[i-1][rest] + value > dp[i-1][j]:
                dp[i][j] = dp[i-1][rest] + value
            else:
                dp[i][j] = dp[i-1][j]
print(dp[-1][-1])

import sys
read = sys.stdin.readline

ans = []
dp = [[0] * (1001) for _ in range(1001)]
nums = [1, 2, 3]
dp[0][0] = 1
for i in range(1, 1001):
    dp[i][0] = 1
    for j in range(1, 1001):
        for k in range(3):
            if j - nums[k] >= 0:
                dp[i][j] += dp[i-1][j-nums[k]]
for _ in range(int(read())):
    n, m = map(int, read().split())
    ans.append(dp[m][n] % 1000000009)
print(*ans, sep='\n')
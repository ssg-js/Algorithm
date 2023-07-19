dp = [0, 0, 1, 2]
n = int(input())
for i in range(4, n + 1):
    dp.append(((i-1) * (dp[i-1] + dp[i-2])) % 1000000000)
print(dp[n])
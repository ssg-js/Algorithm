import sys
read = sys.stdin.readline

n = int(read())
stairs = [int(read()) for _ in range(n)]
jumps = [1, 2]
dp = [[[0, False], [0, False]] for _ in range(n)]
dp[n-1] = [[stairs[n-1], False], [stairs[n-1], False]]

for i in range(n-2, -1, -1):
    
    if i + 1 < n:
        for k in range(2):
            if dp[i + 1][k][1] == True: continue
            
            dp[i][0][0] = max(dp[i][0][0], dp[i+1][k][0] + stairs[i])
            dp[i][0][1] = True
    
    if i + 2 < n:
        for k in range(2):
            dp[i][1][0] = max(dp[i][1][0], dp[i+2][k][0] + stairs[i])
            
ans = max(dp[0][0][0], dp[0][1][0])
if n > 1:
    ans = max(ans, dp[1][0][0], dp[1][1][0])
print(ans)
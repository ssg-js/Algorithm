# 56분
import sys
read = sys.stdin.readline
# (n//m)C1 + (n//m-1)Cm + (n//m-2)Cm => O(n^3) 이므로 시간초과
n = int(read())
arr = [*map(int, read().split())]
k = int(read())
# 합 배열 만들기
s = [0] * n
s[0] = arr[0]
for i in range(1, n):
    s[i] = s[i-1] + arr[i]
dp = [[0]*n for _ in range(3)] # 1, 2, 3개 고르는 데 현재 idx까지 최대 승객수
# 첫줄처리
dp[0][k-1] = s[k-1]
for j in range(k, n):
    dp[0][j] = max(dp[0][j-1], s[j]-s[j-k])
for i in range(1, 3): # O(n)...!!!
    for j in range(k*(i+1)-1, n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-k]+s[j]-s[j-k])
print(dp[2][n-1])


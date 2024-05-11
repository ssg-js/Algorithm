import sys
read = sys.stdin.readline
n, m = map(int, read().split())
str1 = read().rstrip()
str2 = read().rstrip()
dp = [[0] * n for _ in range(m)] # 가로 str1, 세로 str2 로 두고 dp
# 첫 줄 초기화
dp[0][0] = abs(ord(str1[0])-ord(str2[0]))
for i in range(1, m):
    dp[i][0] = dp[i-1][0] + abs(ord(str1[0]) - ord(str2[i])) # str1 첫번째 글자 늘려서 누적한 값 채우기
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + abs(ord(str1[j]) - ord(str2[0]))
# dp 채우기
for i in range(1, m):
    for j in range(1, n):
        # str1 현재 알파벳 늘림, str2 현재 알파벳 늘림, 둘다 안늘리고 추가 + 현재 위치 두 알파벳 다른만큼 추가로 더해줘야함
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + abs(ord(str1[j]) - ord(str2[i]))
print(dp[m-1][n-1])

import sys
read = sys.stdin.readline
n = int(read())
arr = [*map(int, read().split())]
s = [0] * n
s[0] = arr[0]
for i in range(1, n):
    s[i] = s[i-1] + arr[i]
# 벌벌 꿀, 벌 꿀 벌, 꿀 벌벌 형태로 각각 dp 배열을 만들어서 값을 비교
# 벌벌 꿀
dp = [[0] * n for _ in range(2)] # i까지 j마리의 벌을 놓을 때 가질 수 있는 최댓값
for i in range(1, n): # 첫줄
    dp[0][i] = s[i]-s[0]
for i in range(2, n):
    dp[1][i] = max(dp[0][i]-arr[i-1]+arr[i], dp[1][i-1]+2*arr[i]) # (i-1자리에 두번째 벌 추가), (이전최대케이스+숫자만 추가)
ans = dp[1][n-1]
# 벌 꿀 벌
dp[1] = [0] * n # 이전 첫 번째 줄 살림
for i in range(2, n):
    dp[1][i] = max(dp[0][i-1]+arr[i-1], dp[1][i-1]+arr[i-1]) # (벌 .. 꿀벌 케이스), (이전최대케이스+숫자추가하면서 벌 이동)
ans = max(ans, dp[1][n-1])
# 꿀 벌벌 => 벌벌 꿀 같은 로직으로 arr 반대 배열 돌리면 됨
arr.reverse()
s = [0] * n
s[0] = arr[0]
for i in range(1, n):
    s[i] = s[i-1] + arr[i]
dp = [[0] * n for _ in range(2)]
for i in range(1, n): # 첫줄
    dp[0][i] = s[i]-s[0]
for i in range(2, n):
    dp[1][i] = max(dp[0][i]-arr[i-1]+arr[i], dp[1][i-1]+2*arr[i])
ans = max(ans, dp[1][n-1])
print(ans)


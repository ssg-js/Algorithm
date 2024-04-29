import sys
read = sys.stdin.readline
n = int(read())
t = []
p = []
for _ in range(n):
    a, b = map(int, read().split())
    t.append(a)
    p.append(b)
dp = [0 for _ in range(n+1)]
for i in range(n):
    if i > 0:
        dp[i] = max(dp[i-1], dp[i]) # 이전 최댓값 꾸준히 갱신
    ni = i+t[i]
    np = dp[i]+p[i]
    if ni < n+1:
        dp[ni] = max(dp[ni], np)
print(max(dp))
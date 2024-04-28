import sys
read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))
dp = [1 for _ in range(n)] # 현재 idx까지 가장 긴 길이 저장
max_idx = 0 # 가장 길이가 긴 증가 수열 끝 idx
max_dp = 1 # 가장 길이간 긴 증가 수열 길이
for i in range(n):
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
    if max_dp < dp[i]:
        max_dp = dp[i]
        max_idx = i
lis = [arr[max_idx]]
max_idx -= 1
max_dp -= 1
while max_dp > 0:
    if arr[max_idx] < lis[-1] and max_dp == dp[max_idx]:
        lis.append(arr[max_idx])
        max_dp -= 1
    max_idx -= 1
lis.reverse()
print(len(lis))
print(*lis)
    
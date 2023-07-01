N = int(input())
numbers = list(map(int, input().split()))

# dfs로 품 -> 시간초과
# case = []
# max = 0
#
#
# def dfs(now, i):
#     global max
#     # numbers 끝까지 다 수행했으면 갯수 구하고 끝!
#     if i == len(numbers):
#         if len(case) > max:
#             max = len(case)
#         return
#     # 고르고 넘어가기
#     if numbers[i] > now:
#         case.append(numbers[i])
#         dfs(numbers[i], i + 1)
#         case.pop()
#     # 안고르고 넘어가기
#     # -> case에 담긴 수보다 크지만 고르지 않은 경우
#     # -> case에 담긴 수보다 작은 경우
#     dfs(now, i + 1)
#
#
# dfs(0, 0)
# print(max)

# dp
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))

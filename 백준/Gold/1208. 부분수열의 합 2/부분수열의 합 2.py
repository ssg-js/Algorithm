import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
read = sys.stdin.readline
n, s = map(int, read().split())
arr = [*map(int, read().split())]
arr1 = arr[:n//2]
arr2 = arr[n//2:]
sum1 = []
sum2 = []
ans = 0
for k in range(1, n//2+2):
    for combination in combinations(arr1, k):
        v = sum(combination)
        sum1.append(v)
        if v == s:
            ans += 1
    for combination in combinations(arr2, k):
        v = sum(combination)
        sum2.append(v)
        if v == s:
            ans += 1
sum1.sort()
sum2.sort()
# 조합
for v in sum1:
    target = s - v
    left = bisect_left(sum2, target)
    if left < len(sum2):
        ans += bisect_right(sum2, target) - left
print(ans)




import sys
from bisect import bisect_left
read = sys.stdin.readline
n = int(input())
arr = list(map(int, read().split()))
LIS = [arr[0]]
for v in arr:
    if LIS[-1] < v:
        LIS.append(v)
    elif LIS[-1] > v:
        idx = bisect_left(LIS, v)
        LIS[idx] = v
print(len(LIS))

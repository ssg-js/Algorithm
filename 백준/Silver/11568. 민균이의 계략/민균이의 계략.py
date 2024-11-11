import sys
from bisect import bisect_left
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))

lis = []
for v in arr:
    if len(lis) == 0:
        lis.append(v)
        continue

    if v > lis[-1]:
        lis.append(v)
        continue

    idx = bisect_left(lis, v)
    lis[idx] = v    
print(len(lis))

import sys
from bisect import bisect_left, bisect_right;
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
iter = arr[:]
arr = list(set(arr))
arr.sort()

for v in iter:
    print(bisect_left(arr, v), end=" ")
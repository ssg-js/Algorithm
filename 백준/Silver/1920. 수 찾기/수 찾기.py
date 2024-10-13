import sys
from bisect import bisect_left;
read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))
arr.sort()
m = int(read())

for v in list(map(int, read().split())):
    idx = bisect_left(arr, v)
    if idx < n and arr[idx] == v:
        print(1)
    else:
        print(0)
import sys
from bisect import bisect_left, bisect_right;
read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))
arr.sort()
m = int(read())

for v in list(map(int, read().split())):
    print(bisect_right(arr, v) - bisect_left(arr, v), end=" ")
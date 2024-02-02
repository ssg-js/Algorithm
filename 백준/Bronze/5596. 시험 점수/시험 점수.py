import sys
a = sum(map(int, sys.stdin.readline().split()))
b = sum(map(int, sys.stdin.readline().split()))
if b > a:
    print(b)
else:
    print(a)
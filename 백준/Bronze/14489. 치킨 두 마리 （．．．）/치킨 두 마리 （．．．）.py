import sys
read = sys.stdin.readline
a, b = map(int, read().split())
price = int(read())
v = a + b - price * 2
if v >= 0:
    print(v)
else:
    print(a + b)
import sys
n, k = map(int, sys.stdin.readline().split())
for i in range(1, n + 1):
    if n % i == 0:
        k -= 1
    if k == 0:
        print(i)
        break
else:
    print(0)
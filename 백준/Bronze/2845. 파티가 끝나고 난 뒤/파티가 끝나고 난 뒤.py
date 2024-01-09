import sys
read = sys.stdin.readline

L, P = map(int, read().split())
num = list(map(int, read().split()))
minus = L * P

for n in num:
    print(n - minus, end=' ')
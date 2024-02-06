import sys
read = sys.stdin.readline

while True:
    m, n = map(int, read().split())
    if m == 0 and n == 0:
        break
    print(m+n)
import sys
read = sys.stdin.readline
n, k = map(int, read().split())
ans = 0
while bin(n).count('1') > k:
    i = bin(n)[::-1].index('1')
    ans += 2**i
    n += 2**i
print(ans)
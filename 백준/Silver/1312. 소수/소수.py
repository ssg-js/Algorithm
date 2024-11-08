import sys
read = sys.stdin.readline

a, b, n = map(int, read().split())
print(((a*(10**n))//b) % 10)
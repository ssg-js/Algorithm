import sys
n = int(sys.stdin.readline())
ans = 'long ' * ((n - 1) // 4 + 1) + 'int'
print(ans)
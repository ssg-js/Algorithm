import sys
for i in range(1, int(input()) + 1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #', i, ': ', a, ' + ', b, ' = ', a+b, sep='')
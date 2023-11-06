import sys
for _ in range(3):
    n = int(sys.stdin.readline())
    ans = 0
    for _ in range(n):
        ans += int(sys.stdin.readline())
    if ans < 0:
        print('-')
    elif ans > 0:
        print('+')
    else:
        print('0')
import sys
a, b = map(int, sys.stdin.readline().split())
cnt = 0
while a != b:
    if b == 0:
        break
    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b = b // 2
    else:
        break
    cnt += 1
if a == b:
    print(cnt + 1)
else:
    print(-1)
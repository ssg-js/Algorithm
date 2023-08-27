import sys
num = [False] * 31
for i in range(28):
    a = int(sys.stdin.readline())
    num[a] = True
for i in range(1, len(num)):
    if not num[i]:
        print(i)
import sys
read = sys.stdin.readline
for i in range(1, int(read()) + 1):
    s = read().rstrip()
    print(f'{i}. {s}')
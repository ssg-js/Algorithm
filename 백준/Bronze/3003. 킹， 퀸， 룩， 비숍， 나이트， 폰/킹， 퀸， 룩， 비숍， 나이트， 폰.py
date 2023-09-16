import sys
right = [1, 1, 2, 2, 2, 8]
print(*map(lambda x:x[1] - x[0], zip(list(map(int, sys.stdin.readline().split())), right)))
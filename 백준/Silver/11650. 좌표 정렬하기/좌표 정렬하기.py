import sys
N = int(sys.stdin.readline())
ans = []
for _ in range(N):
    ans.append(tuple(map(int, sys.stdin.readline().split())))
ans.sort()
for pair in ans:
    print(*pair)
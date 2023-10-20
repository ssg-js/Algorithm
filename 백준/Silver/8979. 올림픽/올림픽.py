import sys
N, K = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
info.sort(key=lambda x: x[1:], reverse=True)
for i in range(0, N):
    if info[K-1][1:] == info[i][1:]:
        break
print(i+1)
import sys
N, K = map(int, sys.stdin.readline().split())
info = dict()
for _ in range(N):
    num, *arr = (map(int, sys.stdin.readline().split()))
    info[num] = arr
n_info = sorted(info.items(), key=lambda x: x[1], reverse=True)
for i in range(0, N):
    if info[K] == n_info[i][1]:
        break
print(i+1)
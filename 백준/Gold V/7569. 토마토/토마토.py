import sys
from collections import deque
from collections import deque
read = sys.stdin.readline
m, n, h = map(int, read().split())
board = [[list(map(int, read().split())) for _ in range(n)] for _ in range(h)]
cnt = 0
day = 1
target_v = n * m * h
queue = deque()
# find rotten tomato
for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 1:
                queue.append((k, i, j))
                cnt += 1
            elif board[k][i][j] == -1:
                target_v -= 1
d = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
if cnt == target_v: # already over
    print(0)
else:
    while queue:
        for _ in range(len(queue)):
            k, i, j = queue.popleft()
            for dk, di, dj in d:
                nk, ni, nj = k+dk, i+di, j+dj
                if 0 <= nk < h and 0 <= ni < n and 0 <= nj < m and board[nk][ni][nj] == 0:
                    queue.append((nk, ni, nj))
                    board[nk][ni][nj] = 1
                    cnt += 1
            if cnt == target_v:
                break
        else:
            day += 1
    if cnt == target_v:
        print(day)
    else:
        print(-1)
import sys
from collections import deque
read = sys.stdin.readline
n, m = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
cnt = 0
ans = 0
for idx in range(n*m):
    i, j = idx // m, idx % m
    if visited[i][j] or board[i][j] == 0:
        continue
    queue = deque([(i, j)])
    visited[i][j] = True
    tmp = 0
    while queue:
        x, y = queue.popleft()
        tmp += 1
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 1:
                    queue.append((nx, ny))
    cnt += 1
    if ans < tmp:
        ans = tmp
print(cnt)
print(ans)

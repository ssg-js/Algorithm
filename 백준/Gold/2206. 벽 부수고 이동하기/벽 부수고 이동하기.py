import sys
from collections import deque
read = sys.stdin.readline
n, m = map(int, read().split())
board = [list(map(int, list(read().rstrip()))) for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
queue = deque([(0, 0, 0)])
ans = -1
while queue:
    i, j, no_chance = queue.popleft()
    if i == n-1 and j == m-1:
        ans = visited[i][j][no_chance]
        break
    for di, dj in d:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < m:
            if board[ni][nj] == 1 and no_chance == 0:
                visited[ni][nj][1] = visited[i][j][0] + 1
                queue.append((ni, nj, 1))
            elif board[ni][nj] == 0 and visited[ni][nj][no_chance] == 0:
                visited[ni][nj][no_chance] = visited[i][j][no_chance] + 1
                queue.append((ni, nj, no_chance))
print(ans)
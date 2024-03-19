import sys
from collections import deque
read = sys.stdin.readline
n, m = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
ans = 0
flag = False
year = 0
all_zero = False
while not flag and not all_zero:
    iceberg = [] # 한번에 녹이기
    group = 1
    year += 1
    all_zero = True
    visited = [[False] * m for _ in range(n)]
    for idx in range(n*m):
        i, j = idx // m, idx % m
        if board[i][j] == 0 or visited[i][j]:
            continue
        if all_zero:
            all_zero = False
        if group == 2:
            ans = year - 1 # 지금 보드에서 쪼개져 있다는 건 이전 년도에 깨진거
            flag = True
            break
        queue = deque([(i, j)])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            minus = 0
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 0:
                        minus += 1
                    elif not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            iceberg.append((x, y, board[x][y]-minus))
        group += 1
    if flag:
        break
    # 녹이기
    for x, y, v in iceberg:
        if v < 0:
            v = 0
        board[x][y] = v
print(ans)

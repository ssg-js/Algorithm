import sys
from collections import deque
read = sys.stdin.readline
m, n, k = map(int, read().split())
board = [[0]*(m) for _ in range(n)]
for _ in range(k): # paint
    x1, y1, x2, y2 = map(int, read().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
cnt = 0
arr = []
for idx in range(m*n):
    now_x, now_y = idx//m, idx%m
    if board[now_x][now_y] == 0:
        cnt += 1
        area = 0
        queue = deque([(now_x, now_y)])
        board[now_x][now_y] = 1
        while queue: # area count
            x, y = queue.popleft()
            area += 1
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                    board[nx][ny] = 1
                    queue.append((nx, ny))
        arr.append(area)
arr.sort()
print(cnt)
print(*arr)
                    
                    
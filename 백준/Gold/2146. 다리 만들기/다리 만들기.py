import sys
from collections import deque
read = sys.stdin.readline
n = int(read())
board = [[*map(int, read().split())] for _ in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = n*n
# 섬 구분 2부터
island = 2
for num in range(n*n):
    i, j = num//n, num%n
    if board[i][j] == 1:
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            if board[x][y] != 1:
                continue
            board[x][y] = island
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                    queue.append((nx, ny))
        island += 1
# 최소 거리 구하기
for num in range(n*n):
    i, j = num//n, num%n
    if board[i][j] > 1:
        now = board[i][j]
        visited = [[False] * n for _ in range(n)]
        cnt = 0
        queue = deque([(i, j)])
        visited[i][j] = True
        while queue:
            if cnt > ans:
                break
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if board[x][y] != now and board[x][y] > 1:
                    ans = min(ans, cnt-1)
                    break
                for dx, dy in d:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != now and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            cnt += 1
print(ans)
import sys
from collections import deque
read = sys.stdin.readline
n = int(read())
board = [list(read()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def normal_count():
    cnt = 0
    for idx in range(n * n):
        i, j = idx // n, idx % n
        if not visited[i][j]:
            color = board[i][j]
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue: # 같은 구역 방문 처리
                x, y = queue.popleft()
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            cnt += 1 # 한 구역 처리 후 카운트
    return cnt


def weak_count():
    cnt = 0
    for idx in range(n * n):
        i, j = idx // n, idx % n
        if not visited[i][j]:
            color = board[i][j]
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue:  # 같은 구역 방문 처리
                x, y = queue.popleft()
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        if color in ["R", "G"] and board[nx][ny] in ["R", "G"]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                        elif board[nx][ny] == color:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            cnt += 1  # 한 구역 처리 후 카운트
    return cnt


print(normal_count(), end=' ')
visited = [[False] * n for _ in range(n)]
print(weak_count())

import sys
read = sys.stdin.readline
n = int(read())
board = [read().rstrip() for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# 정상
stack = []
visited = [[False]*n for _ in range(n)]
cnt = 0
for idx in range(n*n):
    i, j = idx // n, idx % n
    if visited[i][j]:
        continue
    cnt += 1
    color = board[i][j]
    stack.append((i, j))
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == color:
                    stack.append((nx, ny))
print(cnt, end=' ')
# 적록색약
same = ['R', 'G']
stack = []
visited = [[False]*n for _ in range(n)]
cnt = 0
for idx in range(n*n):
    i, j = idx // n, idx % n
    if visited[i][j]:
        continue
    cnt += 1
    color = board[i][j]
    stack.append((i, j))
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if color in same:
                    if board[nx][ny] in same:
                        stack.append((nx, ny))
                elif board[nx][ny] == color:
                    stack.append((nx, ny))
print(cnt)
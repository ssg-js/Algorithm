import sys
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

height, width, number = map(int, sys.stdin.readline().split())
board = [['.' for _ in range(width)] for _ in range(height)]
visited = [[False] * width for _ in range(height)]
ans = 0
for _ in range(number):
    r, c = map(lambda x: int(x)-1, sys.stdin.readline().split())
    board[r][c] = '#'

queue = deque()
for i in range(height):
    for j in range(width):
        if board[i][j] == '#' and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = True
            cnt = 1
            while queue:
                vi, vj = queue.popleft()
                for d in range(4):
                    ni = vi+di[d]
                    nj = vj+dj[d]
                    if 0 <= ni < height and 0 <= nj < width:
                        if board[ni][nj] == '#' and not visited[ni][nj]:
                            queue.append((ni, nj))
                            visited[ni][nj] = True
                            cnt += 1
            ans = max(ans, cnt)
print(ans)


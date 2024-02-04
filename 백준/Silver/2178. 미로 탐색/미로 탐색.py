import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
board = [read().rstrip() for _ in range(n)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
solved = False

queue = deque()
queue.append((0,0))
move = 1
while queue:
    if solved:
        break
    for _ in range(len(queue)):
        i, j = queue.popleft()
        if i == n - 1 and j == m - 1: # arrive
            print(move)
            solved = True
            break
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m:
                if board[ni][nj] == '1' and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
    move += 1






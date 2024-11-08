import sys
from heapq import heappop, heappush
read = sys.stdin.readline

n, m = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
queue = [(-board[0][0], 0, 0)]
mark = [[0]*m for _ in range(n)]
mark[0][0] = 1

while queue:
    cur, x, y = heappop(queue)
    cur *= -1

    for dx, dy in delta:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] < cur:
            if mark[nx][ny] == 0:
                heappush(queue, (-board[nx][ny], nx, ny))
            mark[nx][ny] += mark[x][y]
print(mark[-1][-1])
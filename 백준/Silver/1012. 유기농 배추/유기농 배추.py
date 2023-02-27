# 유기농 배추
import sys

sys.setrecursionlimit(10000)


def dfs(x, y):
    visited[x][y] = True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and field[nx][ny]:
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, int(input()) + 1):
    m, n, k = map(int, input().split())

    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    total = 0

    for _ in range(k):
        j, i = map(int, input().split())
        field[i][j] = 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and field[i][j] == 1:
                dfs(i, j)
                total += 1

    print(total)
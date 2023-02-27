# 섬의 개수

import sys

sys.setrecursionlimit(10000)


def dfs(x, y):
    visited[x][y] = True

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny] and field[nx][ny] == 1:
            dfs(nx, ny)


# 상, 하, 좌, 우, 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
while True:
    width, height = map(int, input().split())

    if width == 0 and height == 0:
        break

    field = [list(map(int, input().split())) for _ in range(height)]
    visited = [[False] * width for _ in range(height)]
    total = 0

    for i in range(height):
        for j in range(width):
            if not visited[i][j] and field[i][j] == 1:
                dfs(i, j)
                total += 1

    print(total)
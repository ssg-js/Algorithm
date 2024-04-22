import sys
from collections import deque
read = sys.stdin.readline


def dfs(stop_by, now, power):
    global ans
    if ans == len(mincho):
        return
    x, y = now
    if power >= (abs(home[0] - x) + abs(home[1] - y)):  # 집으로 감
        ans = max(len(stop_by), ans)
    for nx, ny in mincho:
        if (nx, ny) in stop_by: # 지난 곳 패스
            continue
        power_sub = power - (abs(nx - x) + abs(ny - y))
        if power_sub >= 0:  # 현재 체력으로 갈 수 있는곳
            dfs(stop_by + [(nx, ny)], (nx, ny), power_sub + plus)  # 이동
    return


# 집 1, 민초 2, 빈땅 0
n, hp, plus = map(int, read().split())
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
board = [list(map(int, read().split())) for _ in range(n)]
mincho = []
ans = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home = (i, j)
        if board[i][j] == 2:
            mincho.append((i, j))
dfs([], home, hp)
print(ans)

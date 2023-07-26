import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
queue = []
day = 0
check = False


def bfs(a, b):
    queue.append((a, b))
    while queue:
        x, y = queue.pop(0)
        visited[x][y] = True
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < n and 0 <= nj < m:
                if board[ni][nj] != 0 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
                elif board[ni][nj] == 0:
                    count[x][y] += 1
    return 1


while True:
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i, j))
    # 깍기
    for i in range(n):
        for j in range(m):
            board[i][j] -= count[i][j]
            if board[i][j] < 0:
                board[i][j] = 0

    if len(result) == 0:
        break
    if len(result) >= 2:
        check = True
        break
    day += 1
    
if check:
    print(day)
else:
    print(0)
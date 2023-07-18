# 1324 - 1348

row, column, length = map(int, input().split())
board = [input() for _ in range(row)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cnt = 0
visited = [[False] * column for _ in range(row)]


def go(x, y, depth):
    global row, column, cnt
    if depth == 1:
        if x == 0 and y == column-1:
            cnt += 1
        return
    if x == 0 and y == column-1:
        return
    visited[x][y] = True
    for d in range(4):
        ni = x + di[d]
        nj = y + dj[d]
        if 0 <= ni < row and 0 <= nj < column:
            if not visited[ni][nj] and board[ni][nj] != 'T':
                go(ni, nj, depth - 1)
    visited[x][y] = False


go(row-1, 0, length)
print(cnt)
import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dfs(x, y, h):
    for d in range(4):
        ni = x + di[d]
        nj = y + dj[d]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and board[ni][nj] > h:
            visited[ni][nj] = True
            dfs(ni, nj, h)


ans = 1
for k in range(max(map(max, board))):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > k and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                dfs(i, j, k)
    ans = max(ans, cnt)

print(ans)



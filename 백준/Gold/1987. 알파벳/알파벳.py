import sys
read = sys.stdin.readline
n, m = map(int, read().split())
board = [read().rstrip() for _ in range(n)]
ans = 1
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False]*m for _ in range(n)]
visited[0][0] = True


def dfs(x=0, y=0, s=board[0][0]):
    global ans
    if ans == 26:
        return
    ans = max(ans, len(s))
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if board[nx][ny] in s:
                continue
            else:
                visited[nx][ny] = True
                dfs(nx, ny, s+board[nx][ny])
                visited[nx][ny] = False
                
                
dfs()
print(ans)
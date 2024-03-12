import sys
read = sys.stdin.readline

n, m = map(int, read().split())
board = [read().rstrip() for _ in range(n)] # 알파벳 입력받기
ans = 1 # 시작점부터 카운트
d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 4방향


def dfs(x=0, y=0, s=board[0][0]):
    global ans
    if ans == 26: # 최대 26글자임
        return
    ans = max(ans, len(s))
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] not in s:
            dfs(nx, ny, s + board[nx][ny])


dfs()
print(ans)
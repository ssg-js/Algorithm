def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = True

    for d in range(4):
        fx = x + dx[d]
        fy = y + dy[d]

        if 0 <= fx < n and 0 <= fy < n and not visited[fx][fy] and plane[fx][fy] == 1:
            dfs(fx, fy)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
plane = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and plane[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

result.sort()
print(len(result))
print(*result, sep='\n')

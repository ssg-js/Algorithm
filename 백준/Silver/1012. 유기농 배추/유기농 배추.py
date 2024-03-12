import sys
read = sys.stdin.readline
for _ in range(int(read())): # 테스트 케이스
    m, n, k = map(int, read().split())
    board = [[0]*m for _ in range(n)] # 밭 상태
    ans = 0
    for _ in range(k):
        x, y = map(int, read().split())
        board[y][x] = 1
    visited = [[False] * m for _ in range(n)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for idx in range(m*n):
        i, j = idx // m, idx % m
        if board[i][j] == 0 or visited[i][j]:
            continue
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        stack.append((nx, ny))
        ans += 1
    print(ans)
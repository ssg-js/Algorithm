def solution(land):
    n = len(land)
    m = len(land[0])
    answer = 0
    board = [[[] for _ in range(m)] for _ in range(n)] # (집합값, 총크기)
    visited = [[False] * m for _ in range(n)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)];
    stack = []
    store = []
    # board 만들기
    ab_num = 1
    cnt = 0
    for num in range(n * m):
        i, j = num // m, num % m
        if land[i][j] == 0:
            continue
        if visited[i][j]:
            continue
        stack.append((i, j))
        store.append((i, j))
        visited[i][j] = True
        cnt += 1
        while stack:
            x, y = stack.pop()
            for di, dj in d:
                ni, nj = x+di, y+dj
                if 0 <= ni < n and 0 <= nj < m and land[ni][nj] == 1 and not visited[ni][nj]:
                    cnt += 1
                    stack.append((ni, nj))
                    store.append((ni, nj))
                    visited[ni][nj] = True
        while store:
            x, y = store.pop()
            board[x][y] = (ab_num, cnt)
        store = []
        stack = []
        ab_num += 1
        cnt = 0
    for j in range(m):
        new_visited = set()
        cnt = 0
        for i in range(n):
            if not board[i][j]:
                continue
            num, size = board[i][j]
            if num in new_visited:
                continue
            new_visited.add(num)
            cnt += size
        answer = max(answer, cnt)
    return answer


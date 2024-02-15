import sys
from collections import deque
read = sys.stdin.readline
d = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
for _ in range(int(read())):
    n = int(read())
    start_i, start_j = map(int, read().split())
    end_i, end_j = map(int, read().split())
    visited = [[False]*n for _ in range(n)]
    queue = deque([(start_i, start_j)])
    visited[start_i][start_j] = True # visit 
    cnt = 0
    flag = False
    while queue: # bfs
        for _ in range(len(queue)):
            now_i, now_j = queue.popleft()
            if now_i == end_i and now_j == end_j:
                flag = True
                break
            for di, dj in d:
                ni, nj = now_i+di, now_j+dj
                if 0<=ni<n and 0<=nj<n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
        else:
            cnt += 1
        if flag:
            break
    print(cnt)
    
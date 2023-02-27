# [BOJ] 7576. 토마토

# 0이 있는지 검사
# -1로 막힌 부분이 있는지 검사하기

from collections import deque


def bfs(li):
    global cnt
    queue = deque(li)
    while queue:
        pos = queue.popleft()
        x, y = pos
        for d in range(4):                                                  # 현재 주위 토마토
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and (tomatoes[nx][ny] == 0):
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append([nx, ny])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

arr = []                                                                    # 예) [[1, 2], [2, 3]]
result = 0
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:                                             # 익은 토마토 만나면
            arr.append([i, j])                                              # 해당 좌표 저장
bfs(arr)

for tomato in tomatoes:                                                     # 다 익은 후 안 익은 토마토면
    if 0 in tomato:
        result = 0                                                             # 결과 -1
        break
    for each in tomato:
        if each > result:
            result = each

print(result - 1)




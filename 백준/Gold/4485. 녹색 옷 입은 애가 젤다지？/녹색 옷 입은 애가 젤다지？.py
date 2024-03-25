import sys
from heapq import heappop, heappush
read = sys.stdin.readline
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dijkstra(arr, queue, information):
    visited = [[False] * n for _ in range(n)]
    while queue:
        cur_value, cur_i, cur_j = heappop(queue)
        if visited[cur_i][cur_j]:
            continue
        visited[cur_i][cur_j] = True
        for di, dj in d:
            ni, nj = cur_i+di, cur_j+dj
            if 0 <= ni < n and 0 <= nj < n:
                distance = cur_value + information[ni][nj]
                if arr[ni][nj] > distance:
                    arr[ni][nj] = distance
                if arr[ni][nj] != INF:
                    heappush(queue, (arr[ni][nj], ni, nj))


INF = 987654321
t = 1
while True:
    n = int(read())
    if n == 0:
        break
    board = [list(map(int, read().split())) for _ in range(n)]
    lost = [[INF] * n for _ in range(n)]
    lost[0][0] = board[0][0]
    pq = [(board[0][0], 0, 0)]
    dijkstra(lost, pq, board)
    print('Problem ', t, ': ', lost[n-1][n-1], sep='')
    t += 1






import sys
from heapq import heappop, heappush
read = sys.stdin.readline
INF = 300000 * 10
v, e = map(int, read().split())
start = int(read())
board = [[] for _ in range(v+1)]
for _ in range(e):
    a, d, w = map(int, read().split())
    board[a].append((d, w))
dis = [INF] * (v+1)
# dijkstra
dis[start] = 0
heap = [(0, start)]
while heap:
    now_d, now_n = heappop(heap)
    if now_d > dis[now_n]:
        continue
    for next_n, next_d in board[now_n]:
        if dis[next_n] > now_d + next_d:
            dis[next_n] = now_d + next_d
            heappush(heap, (now_d + next_d, next_n))
for d in dis[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)
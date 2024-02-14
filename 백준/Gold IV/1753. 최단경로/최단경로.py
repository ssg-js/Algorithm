import sys
from heapq import heappop, heappush
read = sys.stdin.readline
INF = 300000 * 10
v, e = map(int, read().split())
start = int(read())
board = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, w = map(int, read().split())
    board[a].append((b, w))
dis = [INF] * (v+1)
dis[start] = 0
heap = [(0, start)]
while heap:
    now_w, now_n = heappop(heap)
    if dis[now_n] < now_w:
        continue
    for next_n, next_w in board[now_n]:
        if dis[next_n] > now_w + next_w:
            dis[next_n] = now_w + next_w
            heappush(heap, (now_w + next_w, next_n))
for ans in dis[1:]:
    if ans == INF:
        print("INF")
    else:
        print(ans)
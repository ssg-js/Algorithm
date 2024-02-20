import sys
from heapq import heappop, heappush
read = sys.stdin.readline
INF = 100 * 100000
n = int(read())
m = int(read())
info = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, read().split())
    info[s].append((e, w))

    
def dijkstra(start):
    heap = [(0, start)]
    d = [INF] * (n+1)
    d[start] = 0
    visited = [False] * (n+1)
    while heap:
        w, end = heappop(heap)
        if visited[end]:
            continue
        visited[end] = True
        for next_idx, next_w in info[end]:
            if not visited[next_idx]:
                if d[next_idx] > w + next_w:
                    d[next_idx] = w + next_w
                    heappush(heap, (w + next_w, next_idx))
    for i in range(len(d)):
        if d[i] == INF:
            d[i] = 0
    return d[1:]


for i in range(1, n+1):
    print(*dijkstra(i))
    

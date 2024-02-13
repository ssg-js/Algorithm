import sys
from heapq import heappush, heappop

read = sys.stdin.readline
v_max = 300000 * 10

v, e = map(int, read().split())
start = int(read())
board = [[] for _ in range(v+1)]

for _ in range(e):  # 간선 정보 입력
    a, b, w = map(int, read().split())
    board[a].append((w, b))


def dijkstra(s):
    visited = [False] * (v+1)
    d = [v_max] * (v+1)
    d[s] = 0
    heap = [(0, s)]
    while heap:
        weight, node = heappop(heap)
        if visited[node]:
            continue
        visited[node] = True

        if weight > d[node]:
            continue

        # 갱신
        for n_w, n_b in board[node]:
            if d[n_b] > weight + n_w:
                d[n_b] = weight + n_w
                heappush(heap, (weight + n_w, n_b))
    return d[1:]


for ans in dijkstra(start):
    if ans == v_max:
        print("INF")
    else:
        print(ans)
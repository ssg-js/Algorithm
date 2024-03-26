import sys
from heapq import heappop, heappush
read = sys.stdin.readline


def dijkstra(arr, queue, information):
    visited = [False] * (n+1)
    while queue:
        cur_value, cur_node = heappop(queue)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        for next_dis, next_node in information[cur_node]:
            distance = cur_value + next_dis
            if arr[next_node] > distance:
                arr[next_node] = distance
            if arr[next_node] != INF:
                heappush(queue, (arr[next_node], next_node))


INF = 987654321
for _ in range(int(read())):
    n, d, start = map(int, read().split())
    edge = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, read().split())
        edge[b].append((s, a))
    heap = [(0, start)]
    dis = [INF] * (n+1)
    dis[start] = 0
    dijkstra(dis, heap, edge)
    cnt = 0
    time = 0
    for d in dis:
        if d != INF:
            cnt += 1
            if d > time:
                time = d
    print(cnt, time)






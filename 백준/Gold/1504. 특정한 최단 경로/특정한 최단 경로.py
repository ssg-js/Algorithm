import sys
from heapq import heappop, heappush
read = sys.stdin.readline


def dijkstra(arr, queue, information):
    visited = [False] * (n+1)
    while queue:
        cur_distance, cur_node = heappop(queue)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        for next_node, next_distance in information[cur_node]:
            distance = cur_distance + next_distance
            if arr[next_node] > distance:
                arr[next_node] = distance
            if arr[next_node] != INF:
                heappush(queue, (arr[next_node], next_node))


INF = 987654321
n, e = map(int, read().split())
info = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, read().split())
    info[a].append((b, c))
    info[b].append((a, c))
v1, v2 = map(int, read().split())
distance_start = [INF] * (n+1) # 1번에서 v1, v2까지 최단 거리
distance_start[1] = 0
pq = [(distance_start[1], 1)]
dijkstra(distance_start, pq, info)
distance_v = [INF] * (n+1) # v1에서 v2 최단거리
distance_v[v1] = 0
pq = [(0, v1)]
dijkstra(distance_v, pq, info)
distance_end = [INF] * (n+1) # n에서 v1, v2 최단거리
distance_end[n] = 0
pq = [(0, n)]
dijkstra(distance_end, pq, info)
way_one = distance_start[v1] + distance_v[v2] + distance_end[v2] # 1->v1->v2->n
way_two = distance_start[v2] + distance_v[v2] + distance_end[v1] # 1->v2->v1->n
if way_one >= INF and way_two >= INF:
    print(-1)
else:
    print(min(way_one, way_two))





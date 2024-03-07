import sys
from collections import deque
read = sys.stdin.readline
n, e, v = map(int, read().split())
edge = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(e):
    a, b = map(int, read().split())
    edge[a].append(b)
    edge[b].append(a)
for i in range(len(edge)):
    edge[i].sort()
    
   
def dfs(v, visited, arr):
    if visited[v]:
        return
    visited[v] = True
    print(v, end=' ')
    for next_v in arr[v]:
        if not visited[next_v]:
            dfs(next_v, visited, arr)
    return


def bfs(v, arr):
    queue = deque()
    queue.append(v)
    visited = [False] * (n+1)
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for next_v in arr[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
    return

               
dfs(v, visited, edge)
print()
bfs(v, edge)

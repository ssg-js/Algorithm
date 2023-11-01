import sys

N = int(sys.stdin.readline())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
root = 1
edges = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
visited = [False] * (N + 1)
for info in infos:      # 간선 정보 노드별 저장
    a, b = info[0], info[1]
    edges[a].append(b)
    edges[b].append(a)
# dfs로 루트에서 시작하며 부모노드 저장
stack = [1]
while stack:
    node = stack.pop()
    visited[node] = True
    for next_n in edges[node]:
        if not visited[next_n]:
            stack.append(next_n)
            parents[next_n] = node
for parent in parents[2:]:
    print(parent)



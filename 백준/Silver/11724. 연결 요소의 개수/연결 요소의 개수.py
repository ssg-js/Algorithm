import sys
read = sys.stdin.readline

n, m = map(int, read().split())
edge = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, read().split())
    edge[a].append(b)
    edge[b].append(a)
    

def dfs(idx): # 방문 처리
    if visited[idx]:
        return
    visited[idx] = True
    for v in edge[idx]:
        dfs(v)
    return


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)
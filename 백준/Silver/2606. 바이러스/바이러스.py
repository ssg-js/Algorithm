def dfs(v):
    global cnt
    passed[v] = True

    for next_v in graph[v]:
        if not passed[next_v]:
            cnt += 1
            dfs(next_v)


computers = int(input())
lines = int(input())
graph = [[] for _ in range(computers+1)]
passed = [False] * (computers + 1)
cnt = 0

for i in range(lines):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(cnt)

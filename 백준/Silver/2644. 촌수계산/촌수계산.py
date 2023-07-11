n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
info = dict()
max_num = 0
for _ in range(m):
    a, b = map(int, input().split())
    max_num = max([max_num, a, b])
    if a in info:
        info[a].append(b)
    else:
        info[a] = [b]
    if b in info:
        info[b].append(a)
    else:
        info[b] = [a]
visited = [False] * (max_num + 1)


# bfs
def find(start, end):
    queue = [start]
    visited[start] = True
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            temp = queue.pop(0)
            if temp in info:
                for t in info[temp]:
                    if not visited[t]:
                        queue.append(t)
                        visited[t] = True
        if end in queue:
            return cnt
    return -1


print(find(p1, p2))


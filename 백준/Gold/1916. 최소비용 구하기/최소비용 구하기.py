import sys
read = sys.stdin.readline

inf = 1000 * 100000
v = int(read())
e = int(read())
info = [[inf] * v for _ in range(v)]

for _ in range(e):
    a, b, w = map(int, read().split())
    if w < info[a - 1][b - 1]:
        info[a - 1][b - 1] = w
departure, arrival = map(lambda x: int(x)-1, read().split())
for i in range(v):
    info[i][i] = 0
visited = [False] * v
d = info[departure][:]


def get_small_idx():
    m = inf
    idx = departure
    for k in range(v):
        if not visited[k] and d[k] < m:
            m = d[k]
            idx = k
    return idx


visited[departure] = True
for i in range(v - 1):
    cur = get_small_idx()
    visited[cur] = True
    for j in range(v):
        if not visited[j]:
            if d[cur] + info[cur][j] < d[j]:
                d[j] = d[cur] + info[cur][j]
print(d[arrival])



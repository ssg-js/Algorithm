import sys
from collections import deque
read = sys.stdin.readline
n, m = map(int, read().split())
value = [0] * (n + 1)
edge = [[] for _ in range(n+1)]
ans = []
for _ in range(m):
    a, b = map(int, read().split())
    edge[a].append(b) # 인접 리스트
    value[b] += 1 # 진입 차수 올리기
queue = deque()
for i in range(1, n + 1):
    if value[i] == 0:
        queue.append(i)
while queue:
    idx = queue.popleft()
    ans.append(idx)
    for n_idx in edge[idx]:
        value[n_idx] -= 1 # idx와 연결된 간선 끊으면서 진입 차수 -1
        if value[n_idx] == 0: # 진입 차수가 0인 된 idx 추가
            queue.append(n_idx)
print(*ans)
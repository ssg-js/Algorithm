import sys
from collections import deque
read = sys.stdin.readline
n, k = map(int, read().split())
ans = 0
solved = False
visited = [False] * 100001

queue = deque([n])
while queue:
    if solved:
        break
    for _ in range(len(queue)):
        cur = queue.popleft()
        visited[cur] = True
        if cur == k:
            solved = True
            break
        for nv in [cur-1, cur+1, cur*2]:
            if 0 <= nv < 100001 and not visited[nv]:
                queue.append(nv)
    if not solved:
        ans += 1

print(ans)
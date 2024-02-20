import sys
from collections import deque
read = sys.stdin.readline
s, e = map(int, read().split())
visited = set()
queue = deque([e])
flag = False
cnt = 0
while queue:
    for _ in range(len(queue)):
        n = queue.popleft()
        visited.add(n)
        if n == s:
            flag = True
            break
        if n + 1 not in visited:
            queue.append(n+1)
        if n-1 >= 0 and n-1 not in visited:
            queue.append(n-1)
        while n >= s and n % 2 == 0:
            n = n // 2
            if n == s:
                flag = True
                break
            if n + 1 not in visited:
                queue.append(n + 1)
            if n-1 >= 0 and n-1 not in visited:
                queue.append(n - 1)
        if flag:
            break
    if flag:
        break
    cnt += 1
print(cnt)
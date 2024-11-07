import sys
from collections import deque, defaultdict
read = sys.stdin.readline

n, m = map(int, read().split())
ladders = defaultdict(int)
snakes = defaultdict(int)
for _ in range(n):
    s, e = map(int, read().split())
    ladders[s] = e
for _ in range(m):
    s, e = map(int, read().split())
    snakes[s] = e

def solve():
    queue = deque([1])
    visited = [False] * 101
    cnt = 0
    visited[0] = True
    visited[1] = True
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x = queue.popleft()
            for d in range(1, 7):
                nx = x + d
                if 1 > nx or nx > 100: continue
                if visited[nx]: continue

                if nx in ladders:
                    nx = ladders[nx]
                elif nx in snakes:
                    nx = snakes[nx]
                if visited[nx]: continue
                if nx == 100:
                    print(cnt)
                    return

                visited[nx] = True
                queue.append(nx)
        
solve()

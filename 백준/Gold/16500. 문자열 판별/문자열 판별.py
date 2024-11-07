import sys
from collections import deque
read = sys.stdin.readline

s = read().strip()
n = int(read())
arr = [read().strip() for _ in range(n)]

def solve():
    queue = deque([0])
    visited = [False] * len(s)
    visited[0] = True

    while queue:
        idx = queue.popleft()

        for word in arr:
            if idx + len(word) > len(s): continue
            if word != s[idx: idx+len(word)]: continue
            nIdx = idx+len(word)
            if nIdx == len(s):
                print(1)
                return
            if visited[nIdx]: continue
            visited[nIdx] = True
            queue.append(nIdx)

    print(0)
    return

solve()
        


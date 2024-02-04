import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
board = [list(read().rstrip()) for _ in range(n)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
solved = False

queue = deque([(0, 0)])
move = 1
while queue:
    if solved:
        break
    for _ in range(len(queue)):
        if solved:
            break
        i, j = queue.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if i == n - 1 and j == m - 1:  # arrive
                print(move)
                solved = True
                break
            if 0 <= ni < n and 0 <= nj < m:
                if board[ni][nj] == '1':
                    queue.append((ni, nj))
                    board[ni][nj] = '0'
    move += 1


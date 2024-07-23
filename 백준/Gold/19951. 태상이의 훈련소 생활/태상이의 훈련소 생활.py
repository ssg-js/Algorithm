import sys
read = sys.stdin.readline

n, m = map(int, read().split())
board = list(map(int, read().split()))
state = [0] * n

for _ in range(m):
    s, e, v = map(int, read().split())
    s -= 1
    e -= 1
    state[s] += v
    if e+1 < n:
        state[e+1] += -v

if n > 1:
    print(board[0]+state[0], end=' ')
else:
    print(board[0]+state[0])
    
for i in range(1, n):
    state[i] = state[i-1]+state[i]
    if i < n-1:
        print(board[i]+state[i], end=' ')
    else:
        print(board[i]+state[i])
    
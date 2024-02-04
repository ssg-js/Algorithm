import sys
read = sys.stdin.readline

n, m = map(int, read().split())
board = [list(read().rstrip()) for _ in range(n)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs():
    queue = [(0, 0)]
    move = 1
    while queue:
        temp = []
        for i, j in queue:
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if i == n - 1 and j == m - 1:  # arrive
                    return move
                if 0 <= ni < n and 0 <= nj < m:
                    if board[ni][nj] == '1':
                        temp.append((ni, nj))
                        board[ni][nj] = '0'
        queue = temp
        move += 1


print(bfs())



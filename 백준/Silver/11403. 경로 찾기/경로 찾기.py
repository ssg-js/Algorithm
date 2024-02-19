import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]
visited = [False] * n


def dfs(x):
    for i in range(n):
        if board[x][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i)

            
for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j]:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()
    visited = [False] * n

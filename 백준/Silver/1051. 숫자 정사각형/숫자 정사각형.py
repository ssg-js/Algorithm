import sys, math
read = sys.stdin.readline


n, m = map(int, read().split())
limit = min(n, m)
board = [read().rstrip() for _ in range(n)]

width = 2
value = 1
while width < limit + 1:
    temp = width - 1 # 각 꼭짓점을 구하기 위해 더하는 길이
    for i in range(n-width+1): # 정사각형 왼쪽 위 시작 행값
        for j in range(m-width+1): # 정사각형 왼쪽 위 시작 열값
            if board[i][j] == board[i+temp][j] and board[i][j+temp] == board[i+temp][j+temp] and board[i][j] == board[i][j+temp]:
                value = width
    width += 1
print(value ** 2)



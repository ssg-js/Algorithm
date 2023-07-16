# [BOJ] 10836. 여왕벌
# 소요 시간 : 40분(시간초과)

size, days = map(int, input().split())
board = [[1] * size for _ in range(size)]
growth_info = [list(map(int, input().split())) for _ in range(days)]

for i in range(days):
    plus_board = [[0] * size for _ in range(size)]
    x, y = size - 1, 0
    num_info = []
    num = 0
    for v in growth_info[i]:
        num_info.extend([num] * v)
        num += 1
    for value in num_info:
        plus_board[x][y] = value
        if x == 0:
            y += 1
        else:
            x -= 1
    for a in range(size):
        for b in range(size):
            if a != 0 and b != 0:
                plus_board[a][b] = max(plus_board[a][b - 1], *plus_board[a - 1][b - 1:b + 1])
            board[a][b] += plus_board[a][b]

for i in range(size):
    print(*board[i])
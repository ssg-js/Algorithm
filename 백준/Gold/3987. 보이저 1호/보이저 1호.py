# 45분
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
board = [list(read().rstrip()) for _ in range(n)]
cur_i, cur_j = map(lambda x: int(x)-1, read().split())
ans_table = ['U', 'R', 'D', 'L']
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ans = 0
ans_dir = ans_table[0]
flag = False
for d in range(4):
    first_dir = ans_table[d]
    cnt = 1
    ni, nj = cur_i+di[d], cur_j+dj[d]
    while 0 <= ni < n and 0 <= nj < m and board[ni][nj] != 'C':
        # 무한루프 처리
        if cnt > n * m * 2:
            print(first_dir)
            print('Voyager')
            flag = True
            break
        # 행성 처리
        if board[ni][nj] == '/':
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
        elif board[ni][nj] == '\\':
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 0
        ni += di[d]
        nj += dj[d]
        cnt += 1
    if flag:
        break
    # 최대 방향 처리
    if cnt > ans:
        ans_dir = first_dir
        ans = cnt
if not flag:
    print(ans_dir)
    print(ans)

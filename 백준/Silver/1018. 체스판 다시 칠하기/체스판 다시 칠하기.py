import sys
read = sys.stdin.readline

edge = 8
n, m = map(int, read().split())
board = [read().rstrip() for _ in range(n)]
ans = edge ** 2

for i in range(n - edge + 1):
    for j in range(m - edge + 1): # 시작지점
        # 8 * 8로 자르고 다시칠하는 개수 구함
        before = board[i][j]
        cnt = 0
        for x in range(edge):
            for y in range(edge):
                if x == 0 and y == 0:
                    continue
                if y == 0:
                    if before != board[i+x][j+y]:
                        cnt += 1
                    continue
                if before == board[i+x][j+y]:
                    cnt += 1
                    if board[i+x][j+y] == 'B':
                        before = 'W'
                    else:
                        before = 'B'
                else:
                    before = board[i+x][j+y]
        if cnt > edge ** 2 // 2:
            cnt = edge ** 2 - cnt
        ans = min(ans, cnt)
print(ans)



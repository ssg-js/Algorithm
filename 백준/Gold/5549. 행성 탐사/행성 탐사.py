import sys
read = sys.stdin.readline
n, m = map(int, read().split())
k = int(read())
board = [read().rstrip() for _ in range(n)]
mark = ['J', 'O', 'I']
dp = dict()
for c in mark:
    dp[c] = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        for c in mark:
            if i == 0 and j == 0:
                if board[i][j] == c:
                    dp[c][i][j] = 1
                    continue
                continue
            elif i == 0:
                dp[c][i][j] = dp[c][i][j-1]
                if board[i][j] == c:
                    dp[c][i][j] += 1
            elif j == 0:
                dp[c][i][j] = dp[c][i-1][j]
                if board[i][j] == c:
                    dp[c][i][j] += 1
            else:
                dp[c][i][j] = dp[c][i-1][j] + dp[c][i][j-1] - dp[c][i-1][j-1]
                if board[i][j] == c:
                    dp[c][i][j] += 1
for _ in range(k):
    x1, y1, x2, y2 = map(lambda x: int(x)-1, read().split())
    for c in mark:
        v = dp[c][x2][y2]
        if y1 > 0:
            v -= dp[c][x2][y1 - 1]
        if x1 > 0:
            v -= dp[c][x1-1][y2]
        if x1 > 0 and y1 > 0:
            v += dp[c][x1 - 1][y1 - 1]
        print(v, end=" ")
    print()
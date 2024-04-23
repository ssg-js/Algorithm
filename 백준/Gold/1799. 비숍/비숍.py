import sys
read = sys.stdin.readline


def dfs(point_num=0, cnt=0):
    global ans
    x, y = point_num // n, point_num % n
    if x >= n and y >= 0:
        ans = max(ans, cnt)
        return
    p = 2
    if n % 2 == 0 and y + 2 >= n: # n 짝수인 경우 넘어갈때 흑백 같아지는 문제해결
        if n-y == 2:
            p = 3
        else: # n-y == 1
            p = 1
    if board[x][y] == 1:
        # 대각 검사
        for acc in range(1, max(x, y, n-x, n-y)+1):
            if x-acc >= 0 and y-acc >= 0 and board[x-acc][y-acc] == 2:
                break
            elif x-acc >= 0 and y+acc < n and board[x-acc][y+acc] == 2:
                break
            elif x+acc < n and y-acc >= 0 and board[x+acc][y-acc] == 2:
                break
            elif x+acc < n and y+acc < n and board[x+acc][y+acc] == 2:
                break
        else: # 놓을 수 있으면
            board[x][y] = 2
            dfs(point_num+p, cnt+1)
            board[x][y] = 1
    dfs(point_num+p, cnt)


n = int(input())
board = [list(map(int, read().split())) for _ in range(n)]
ans = 0
dfs()
temp = ans
ans = 0
dfs(1)
ans += temp
print(ans)
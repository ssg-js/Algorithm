import sys


def check():
    for i in range(n):
        now = i
        for horizontal in range(h):
            if board[horizontal][now]: # 오른쪽 연결
                now += 1 # 이동
            elif now > 0 and board[horizontal][now-1]: # 왼쪽 연결
                now -= 1 # 이동
        if now != i: # 틀리면 false 반환
            return False
    return True


def dfs(cnt=0, x=0, y=0):
    global ans
    if cnt > 3 or ans <= cnt:
        return
    if check(): # i -> i 인지 체크
        ans = min(cnt, ans)
        return
    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0
        for j in range(now, n-1): # 오른쪽 끝은 항상 False
            if board[i][j] or (j > 0 and board[i][j-1]) or board[i][j+1]: # 다리설치 불가(오른쪽, 왼쪽, 오른쪽 건너)
                continue
            board[i][j] = True
            dfs(cnt+1, i, j+2)
            board[i][j] = False


read = sys.stdin.readline
n, m, h = map(int, read().split())
board = [[False] * n for _ in range(h)]
not_change = [[False] * n for _ in range(h)] # 주어진 사다리에서 수정할 필요 없는 곳
ans = 4
for _ in range(m):
    a, b = map(lambda x:int(x)-1, read().split())
    board[a][b] = True

dfs()
if ans == 4:
    print(-1)
else:
    print(ans)


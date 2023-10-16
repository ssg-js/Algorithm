# 각 줄마다 정보를 받아서 규칙에 따라 배치

import sys

N = int(sys.stdin.readline())
grid = [[0] * N for _ in range(N)]
stu = 0
likes = [0] * 4
is_empty = [[True] * N for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
seat = []
m_num = 0
info = dict()
ans = 0

def clear():
    global m_num
    m_num = 0


def one():
    global seat, m_num
    check_board = [[0] * N for _ in range(N)]
    temp = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        for p in likes:
                            if grid[ni][nj] == p:
                                check_board[i][j] += 1
                                m_num = max(check_board[i][j], m_num)
                temp.append((i, j))
    for p in temp:
        i, j = p
        if check_board[i][j] == m_num:
            seat.append((i, j))
    clear()
    if len(seat) == 1:
        grid[seat[0][0]][seat[0][1]] = stu
        return True
    else:
        return False


def two():
    global seat, m_num
    n_seat = []
    temp = dict()
    for p in seat:
        i, j = p
        cnt = 0
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if grid[ni][nj] == 0:
                    cnt += 1
        temp[p] = cnt
        m_num = max(cnt, m_num)
    for p, n in temp.items():
        if n == m_num:
            n_seat.append(p)
    clear()
    if len(n_seat) == 1:
        grid[n_seat[0][0]][n_seat[0][1]] = stu
        return True
    else:
        seat = n_seat
        return False


def three():
    grid[seat[0][0]][seat[0][1]] = stu


def set():
    global seat
    if not one():
        if not two():
            three()
    seat = []


for _ in range(N * N):
    stu, *likes = map(int, sys.stdin.readline().split())
    set()
    info[stu] = likes
for i in range(N):
    for j in range(N):
        cnt = 0
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                for p in info[grid[i][j]]:
                    if grid[ni][nj] == p:
                        cnt += 1
        if cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
        else:
            ans += cnt

print(ans)

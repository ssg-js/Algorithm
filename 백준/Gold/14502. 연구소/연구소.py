import sys, copy
from collections import deque

read = sys.stdin.readline
n, m = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]
zero = []
two = []
i = 0
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while i < n * m:
    if board[i // m][i % m] == 0:
        zero.append(i)
    elif board[i // m][i % m] == 2:
        two.append(i)
    i += 1


def combi(arr, cnt):  # 빈 공간 중 3개 반환
    if cnt == 0:
        return [[]]
    result = []
    for idx in range(0, len(arr)):
        for com in combi(arr[idx+1:], cnt - 1):
            result.append([arr[idx]]+com)
    return result


def start(arr, c):  # 해당 case에 대해 시뮬레이션 후 빈 공간 출력
    for idx in c:
        arr[idx // m][idx % m] = 1
    queue = deque()
    for idx in two:
        queue.append((idx // m, idx % m))
    while queue:  # 바이러스퍼짐
        i, j = queue.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                arr[ni][nj] = 2
                queue.append((ni, nj))
    # 안전 구역 세기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    return cnt


ans = 0
for case in combi(zero, 3):
    ans = max(ans, start(copy.deepcopy(board), case))
print(ans)

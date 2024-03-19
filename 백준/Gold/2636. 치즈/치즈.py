import sys
from collections import deque


def get_area(arr):  # 남아있는 공간
    a, b = len(arr), len(arr[0])
    visited = [[False] * b for _ in range(a)]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = 0
    for idx in range(a * b):
        i, j = idx // b, idx % b
        if visited[i][j] or arr[i][j] == 0:
            continue
        visited[i][j] = True
        queue = deque()
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            cnt += 1
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < a and 0 <= ny < b and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if board[nx][ny] == 1:
                        queue.append((nx, ny))
    return cnt


def get_melting(arr, visited, x, y):  # 녹일 공간
    queue = deque()
    queue.append((x, y))
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[x][y] = True
    result = []
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == 0:
                    queue.append((nx, ny))
                if arr[nx][ny] == 1:
                    result.append((nx, ny))
    return result


def melt(arr):  # 녹이기
    visited = [[False] * len(arr[0]) for _ in range(len(arr))]
    to_melt = []
    for i in range(len(arr)):
        if not visited[i][0]:
            to_melt.extend(get_melting(board, visited, i, 0))
        elif not visited[i][len(arr[0]) - 1]:
            to_melt.extend(get_melting(board, visited, i, len(arr[0]) - 1))
    for j in range(len(arr[0])):
        if not visited[0][j]:
            to_melt.extend(get_melting(board, visited, 0, j))
        elif not visited[len(arr) - 1][j]:
            to_melt.extend(get_melting(board, visited, len(arr) - 1, j))
    for x, y in to_melt:
        arr[x][y] = 0
    if len(to_melt) == 0:
        return False
    return True


read = sys.stdin.readline
n, m = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]
hour = 0
size = get_area(board)
while melt(board): # 다 녹을 때까지
    hour += 1
    tmp = get_area(board)
    if tmp != 0:
        size = tmp
print(hour, size, sep='\n')



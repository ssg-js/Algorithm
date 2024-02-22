import sys
from collections import deque
read = sys.stdin.readline
n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]
shark_size = 2


def get_targets(arr, x, y, size): # x, y에서 다음 물고기위치 탐색 후 return, bfs 로 탐색
    width = len(arr) # 굳이 파라미터만 쓰기
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * width for _ in range(width)]
    queue = deque([(x, y)])
    dis = 0
    results = [] # 먹을 수 있는 가장 가까운 애들 좌표, 비었으면 엄마 부름
    end = False
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if 0 < arr[x][y] < size: # 먹을 수 있음
                results.append((x, y, dis)) # return 값 형식
                end = True
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0 <= nx < width and 0 <= ny < width and not visited[nx][ny]:
                    if arr[nx][ny] <= size: # 지나갈 수 있는지
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        if end: # 가장 가까운 목표(들)를 찾았으면 끝
            break
        dis += 1
    return results


def start(arr, x, y, size):
    ans = 0
    to_eat = size
    while True:
        result_x = len(arr) # 나올 수 없는 값
        result_y = len(arr)
        distance = 0
        for now_x, now_y, dis in get_targets(arr, x, y, size): # 하나 고르기
            if distance == 0:
                distance = dis
            if result_x > now_x:
                result_x = now_x
                result_y = now_y
            elif result_x == now_x and result_y > now_y:
                result_x = now_x
                result_y = now_y
        # 엄마 부를 상황
        if result_x == len(arr):
            print(ans)
            return
        # 아니면 계속 진행
        to_eat -= 1
        if to_eat == 0:
            size += 1
            to_eat = size
        arr[result_x][result_y] = 0
        x = result_x
        y = result_y
        ans += distance


end = False
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            start(board, i, j, shark_size)
            end = True
            break
    if end:
        break
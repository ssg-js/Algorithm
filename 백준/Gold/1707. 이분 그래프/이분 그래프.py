import sys
read = sys.stdin.readline
sys.setrecursionlimit(200000)


def check_block(arr, visited, n): # 안되면 True 반환
    for next_i in arr[n]:
        if visited[next_i] > 0 and visited[next_i] == visited[n]: # 방문했었는데 인접 노드가 같은 집합인경우
            return True
        if visited[next_i] == 0:
            if visited[n] == 1:
                visited[next_i] = 2
            else:
                visited[next_i] = 1
            if check_block(arr, visited, next_i):
                return True
    return False


for _ in range(int(read())):
    v, e = map(int, read().split())
    board = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, read().split())
        board[a].append(b)
        board[b].append(a)
    visited = [0] * (v + 1)
    for i in range(1, v+1):
        if visited[i] > 0:
            continue
        visited[i] = 1
        if check_block(board, visited, i):
            print('NO')
            break
    else:
        print('YES')
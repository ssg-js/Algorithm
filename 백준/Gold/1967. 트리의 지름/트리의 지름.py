import sys
from itertools import combinations
sys.setrecursionlimit(10000)
read = sys.stdin.readline
n = int(read())
edge = [[] for _ in range(n+1)]
dp = [[] for _ in range(n+1)] # i번 노드를 지나는 하위 노드들 비용들
for _ in range(n-1):
    a, b, w = map(int, read().split())
    edge[a].append((b, w))


def make_dp(arr, board, node=1): # node 하위 노드로만 ㄱ
    result = []
    for n_node, weight in arr[node]:
        make_dp(arr, board, n_node)
        result.append(weight + max(board[n_node]))
    if not result: # 끝 노드
        result.append(0)
    board[node] = result[:]
    return


def get_ans(board):
    result = 0
    for i in range(1, len(board)): # 상위 노드 부터 하위 노드 연결한 길이 최댓값 계산
        for x, y in combinations(board[i], 2):
            result = max(result, x+y)
        if len(board[i]) == 1:
            result = max(result, board[i][0])
    print(result)
    return


make_dp(edge, dp)
get_ans(dp)

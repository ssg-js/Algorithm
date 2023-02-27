# BOJ_1922. 네트워크 연결 (크루스칼, 프림)


def find_set(node):                                 # root 노드 찾기
    if node != parent[node]:                        # root 노드가 아닐때
        parent[node] = find_set(parent[node])
    return parent[node]


N = int(input())                                    # 컴퓨터의수
M = int(input())                                    # 연결할 수 있는 선의 수
edges = []                                          # 간선 정보 저장

for i in range(M):
    s, e, c = map(int, input().split())             # 시작, 끝, 비용

    edges.append((c, s, e))                         # 비용 순으로 정렬할거라 앞으로 가져와서 append

edges.sort()                                        # 비용 낮은 순 정렬

parent = list(range(N + 1))
count = 0
cost = 0

for dist, x, y in edges:
    root_x, root_y = find_set(x), find_set(y)

    if root_x != root_y:                            # 서로소일때
        parent[root_y] = root_x                     # Union
        count += 1
        cost += dist

    if count >= N - 1:
        break

print(cost)



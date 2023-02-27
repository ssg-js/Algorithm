# BOJ_1976. 여행 가자 (서로소 집합)


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])

    return parent[node]


N = int(input())
M = int(input())
info = [list(map(int, input().split())) for _ in range(N)]      #
travel = list(map(int, input().split()))

parent = list(range(N + 1))                                     # [0, 1, 2, ..., N]

for i in range(N):
    for j in range(i, N):
        if info[i][j] == 1:
            x_root, y_root = find_set(i + 1), find_set(j + 1)           # Find

            if x_root != y_root:                                # 서로소
                if x_root < y_root:
                    parent[y_root] = parent[x_root]
                else:
                    parent[x_root] = parent[y_root]

result = 'YES'
root = find_set(travel[0])
for i in travel:
    if root != find_set(i):
        result = 'NO'
        break

print(result)




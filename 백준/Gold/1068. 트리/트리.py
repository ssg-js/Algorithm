import sys
read = sys.stdin.readline
n = int(read())
table = dict()
info = map(int, read().split())
erase = int(read())
# 노드 등록
for idx, upper_node in enumerate(info):
    if idx == erase or upper_node == erase: # 지울 노드 빼고 추가
        continue
    if upper_node in table: # 상위 노드에 현재 노드(idx) 추가
        table[upper_node].append(idx)
    else:
        table[upper_node] = [idx]
    if idx not in table:
        table[idx] = []
# 리프 노드 탐색
cnt = 0
stack = [-1]
visited = [False] * n
while stack:
    cur = stack.pop()
    if cur not in table:
        continue
    if not table[cur]: # 자식이 비어서 리프노드
        cnt += 1
        continue
    for node in table[cur]:
        if not visited[node]:
            visited[node] = True
            stack.append(node)
print(cnt)
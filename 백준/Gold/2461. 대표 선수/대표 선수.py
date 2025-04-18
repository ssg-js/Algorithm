import sys
read = sys.stdin.readline

import heapq
n, m = map(int, read().split())
students = []
for i in range(n):
    students.append(list(map(int, read().split())))
    students[i].sort()

ans = 1000000000

idx = [0] * n
min_pq = []
max_value = -1
for c in range(n):
    heapq.heappush(min_pq, (students[c][idx[c]], c))
    max_value = max(max_value, students[c][idx[c]])


while True:
    cur_v, cur_c = heapq.heappop(min_pq)
    ans = min(ans, max_value - cur_v)
    if idx[cur_c] < m-1:
        idx[cur_c] += 1
        heapq.heappush(min_pq, (students[cur_c][idx[cur_c]], cur_c))
        max_value = max(max_value, students[cur_c][idx[cur_c]])
    else:
        break

print(ans)

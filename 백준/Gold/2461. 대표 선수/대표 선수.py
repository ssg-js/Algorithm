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


while max(idx) < m:
    ans = min(ans, max_value - min_pq[0][0])
    cur_v, cur_c = heapq.heappop(min_pq)
    idx[cur_c] += 1
    if idx[cur_c] < m:
        heapq.heappush(min_pq, (students[cur_c][idx[cur_c]], cur_c))
        max_value = max(max_value, students[cur_c][idx[cur_c]])
    else:
        break

print(ans)

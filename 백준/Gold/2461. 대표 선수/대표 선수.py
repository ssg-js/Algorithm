import sys
read = sys.stdin.readline

n, m = map(int, read().split())
students = []
for i in range(n):
    students.append(list(map(int, read().split())))
    students[i].sort()

ans = 1000000000

idx = [0] * n

while max(idx) < m:
    
    to_change_class = 0
    max_value = students[0][idx[0]]
    for c in range(1, n):
        if students[c][idx[c]] > max_value:
            max_value = students[c][idx[c]]
        if students[c][idx[c]] < students[to_change_class][idx[to_change_class]]:
            to_change_class = c
    ans = min(ans, max_value - students[to_change_class][idx[to_change_class]])
    idx[to_change_class] += 1

print(ans)

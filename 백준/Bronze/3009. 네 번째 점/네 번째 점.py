import sys
x = dict()
y = dict()
for _ in range(3):
    a, b = sys.stdin.readline().split()
    if a in x.keys():
        x[a] += 1
    else:
        x[a] = 1
    if b in y.keys():
        y[b] += 1
    else:
        y[b] = 1
ans = []
for i, v in x.items():
    if v == 1:
        ans.append(i)
for i, v in y.items():
    if v == 1:
        ans.append(i)
print(*ans)

import sys

n, m = map(int, sys.stdin.readline().split())
root = [i for i in range(n)]
ans = 0


def find(x):
    if root[x] == x:
        return x
    return find(root[x])


def union(x, y):
    global root
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return True
    if rx > ry:
        root[rx] = ry
    else:
        root[ry] = rx


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if union(a, b):
        ans = i + 1
        break
print(ans)

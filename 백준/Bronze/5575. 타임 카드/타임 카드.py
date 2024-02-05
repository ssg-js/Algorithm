import sys
read = sys.stdin.readline

for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, read().split())
    h, m, s = 0, 0, 0
    s = s2 - s1
    if s < 0:
        m -= 1
        s = 60 + s
    elif s > 59:
        m += 1
        s = s - 60
    m = m + m2 - m1
    if m < 0:
        h -= 1
        m = 60 + m
    elif m > 59:
        h += 1
        m = m - 60
    h = h + h2 - h1
    print(h, m, s)
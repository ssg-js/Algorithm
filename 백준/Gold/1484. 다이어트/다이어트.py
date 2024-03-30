import sys
read = sys.stdin.readline
g = int(read())
s, e = 1, 2
fail = True
while s < e:
    sub = e ** 2 - s ** 2
    if sub < g:
        e += 1
    elif sub > g:
        s += 1
    else:
        print(e)
        fail = False
        s += 1
if fail:
    print(-1)

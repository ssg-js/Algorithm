import sys
read = sys.stdin.readline

n = int(read())
info = [(0, [-1])]
for _ in range(n):
    time, *arr = map(int, read().split())
    info.append((time, arr[:-1]))

memo = [-1] * (n+1)


def cal(k):
    if memo[k] > -1:
        return memo[k]
    ret = 0
    for before in info[k][1]:
        ret = max(ret, cal(before))
    ret += info[k][0]
    memo[k] = ret
    return ret


for i in range(1, n+1):
    print(cal(i))


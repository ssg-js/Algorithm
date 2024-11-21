import sys
sys.setrecursionlimit(10000)
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
t = int(read())
memo = [[-1] * n for _ in range(n)]


def bt(preIdx, postIdx):
    if preIdx < 0 or postIdx == len(arr): return 0

    if memo[preIdx][postIdx] != -1: return memo[preIdx][postIdx]

    ret = 0
    if arr[preIdx] == arr[postIdx]:
        ret = 2 + bt(preIdx - 1, postIdx + 1)
    else: ret = max(bt(preIdx, postIdx + 1), ret)
    ret = max(bt(preIdx - 1, postIdx), ret)

    memo[preIdx][postIdx] = ret
    return ret


for _ in range(t):
    m = int(read())-1

    print(n - 1 - bt(m-1, m+1))


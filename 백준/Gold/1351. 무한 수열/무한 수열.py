
import sys
read = sys.stdin.readline
n, p, q = map(int, read().split())
dp = {0: 1}


def solve(k):
    if dp.get(k):
        return dp.get(k)
    v = solve(k//p) + solve(k//q)
    dp[k] = v
    return v


print(solve(n))



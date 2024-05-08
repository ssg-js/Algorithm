
import sys
read = sys.stdin.readline
n = int(read())
dp = [[[0]*(1 << 10) for _ in range(10)] for _ in range(n)]
MOD = 1000000000


def solve(idx, pre, bit): # 현재 idx, 이전 숫자, 상태 비트
    if idx == n:
        if bit == 1023: # 살아남았다는건 성공했다는것
            return 1
        else:
            return 0
    if dp[idx][pre][bit]:
        return dp[idx][pre][bit]
    ret = 0
    if pre - 1 >= 0:
        ret += solve(idx+1, pre-1, bit | (1 << (pre-1))) % MOD
    if pre + 1 < 10:
        ret += solve(idx + 1, pre + 1, bit | (1 << (pre + 1))) % MOD
    ret %= MOD
    dp[idx][pre][bit] = ret
    return ret


cnt = 0
for i in range(1, 10):
    cnt += solve(1, i, 1 << i)
print(cnt % MOD)

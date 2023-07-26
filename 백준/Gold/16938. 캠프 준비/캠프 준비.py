import sys


n, small, big, sub = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0


def combination(array, k):
    result = []

    if k == 0:
        return [[]]
    for idx in range(0, len(array)):
        temp = array[idx]
        rest = array[idx + 1:]
        for com in combination(rest, k - 1):
            result.append([temp] + com)
    return result


for i in range(2, n + 1):
    for c in combination(arr, i):
        if small <= sum(c) <= big:
            if max(c) - min(c) >= sub:
                ans += 1

print(ans)
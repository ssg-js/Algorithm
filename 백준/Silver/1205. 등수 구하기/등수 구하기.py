import sys
read = sys.stdin.readline

n, score, p = map(int, read().split())
arr = list(map(int, read().split()))

def solve():
    if n == 0: return 1

    if p == n and arr[p-1] >= score: return -1

    rank = n + 1
    for i in range(n):
        if arr[i] <= score:
            rank = i+1
            break
    return rank
    

print(solve())
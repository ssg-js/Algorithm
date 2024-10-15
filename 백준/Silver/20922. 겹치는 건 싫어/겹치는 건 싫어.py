import sys
read = sys.stdin.readline

n, k = map(int, read().split())
seq = list(map(int, read().split()))
board = [0] * 100001

l, r = 0, 0
ans = 1

while r < n:
    if l == r:
        board[seq[r]] += 1
        r += 1
        continue

    if board[seq[r]] == k:
        ans = max(ans, r-l)
        while board[seq[r]] == k:
            board[seq[l]] -= 1
            l += 1
    else:
        board[seq[r]] += 1
        r += 1
print(max(ans, r - l))
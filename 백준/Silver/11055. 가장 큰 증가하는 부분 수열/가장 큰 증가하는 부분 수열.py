import sys
read = sys.stdin.readline

n = int(read())
seq = list(map(int,read().split()))

board = [0] * 1000001

for i in range(0, n):
    v = seq[i]
    k = 1
    plus = 0
    while i - k > -1 and v - k > 0:
        if seq[i-k] < v:
            plus = max(plus, board[seq[i-k]])
        plus = max(plus, board[v - k])
        k += 1
    board[seq[i]] = v + plus
print(max(board))

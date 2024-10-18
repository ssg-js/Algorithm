import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())

    if n < 6:
        arr = [0, 1, 1, 1, 2, 2]
        print(arr[n])
    else:
        board = [0] * (n+1)
        board[1] = 1
        board[2] = 1
        board[3] = 1
        board[4] = 2
        board[5] = 2
        for i in range(6, n+1):
            board[i] = board[i-1] + board[i-5]
        print(board[n])

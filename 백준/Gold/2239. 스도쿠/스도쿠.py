# 스도쿠

# 1. 가장 수가 많이 채워진 3 * 3을 찾는다
# 2. 없는 숫자 중 낮은 숫자부터 채워본다
# 3. 같은 행, 같은 열 중 같은 숫자 없는지 판단하고 채운다
# 4. 위와 같은 방법으로 채워간다
# 5. 수를 채울 때마다 다른 분기로 들어간다
# 6.
import sys
sys.setrecursionlimit(10000000)

NUMBER = 9
board = []
zero = 0
# 각 열, 행, 3*3구간에 해당 숫자가 있는지 판별하는 리스트
col = [[False for _ in range(10)] for _ in range(9)]
row = [[False for _ in range(10)] for _ in range(9)]
box = [[False for _ in range(10)] for _ in range(9)]


def square(x, y):
    return (x//3) * 3 + y//3


def sudoku(depth):
    if depth == 81:
        for m in range(NUMBER):
            for n in range(NUMBER):
                print(board[m][n], end='')
            print()
        return True
    x = depth // NUMBER
    y = depth % NUMBER
    if board[x][y] != 0:
        return sudoku(depth + 1)
    else:
        for m in range(1, NUMBER + 1):
            if not col[y][m] and not row[x][m] and not box[square(x, y)][m]:
                col[y][m], row[x][m], box[square(x, y)][m] = True, True, True
                board[x][y] = m
                if sudoku(depth+1):
                    return True
                col[y][m], row[x][m], box[square(x, y)][m] = False, False, False
                board[x][y] = 0
    return False


for i in range(NUMBER):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    for j in range(NUMBER):
        if board[i][j] != 0:
            col[j][board[i][j]] = True
            row[i][board[i][j]] = True
            box[square(i, j)][board[i][j]] = True
        else: # 0이면
            zero += 1
sudoku(0)

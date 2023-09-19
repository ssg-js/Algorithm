import sys
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
ans = [0, (1, 1)]
for i in range(9):
    for j in range(9):
        if arr[i][j] > ans[0]:
            ans = [arr[i][j], (i+1, j+1)]
print(ans[0])
print(*ans[1])
            
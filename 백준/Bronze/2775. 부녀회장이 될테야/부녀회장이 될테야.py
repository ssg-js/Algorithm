import sys
read = sys.stdin.readline
for _ in range(int(read())):
    k = int(read())
    n = int(read())
    cur = [i for i in range(1, n+1)] # 0층
    for i in range(1,n): # 1층 처리
        cur[i] = cur[i] + cur[i-1]
    for _ in range(2, k+1):
        for i in range(1, n):
            cur[i] = cur[i] + cur[i-1]
    print(cur[n-1])
import sys
read = sys.stdin.readline
n = int(read())
A = [*map(int, read().split())]
B = [*map(int, read().split())]
A.sort()
B.sort(reverse=True)
ans = 0
for i in range(n):
    ans += A[i] * B[i]
print(ans)

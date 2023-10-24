import sys
ans = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    ans[int(sys.stdin.readline())] += 1
for i in range(10001):
    for k in range(ans[i]):
        print(i)


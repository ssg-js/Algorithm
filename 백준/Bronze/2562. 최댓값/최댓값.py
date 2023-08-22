import sys
ans = 0
index = 0
for i in range(1, 10):
    num = int(sys.stdin.readline())
    if num > ans:
        ans = num
        index = i
print(ans)
print(index)
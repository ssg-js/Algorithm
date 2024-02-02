import sys
read = sys.stdin.readline

ans = 0
for _ in range(4):
    ans += int(read())
print(ans // 60)
print(ans % 60)
result = int(input())
n = int(input())
cal = 0
for i in range(n):
    cost, vol = map(int, input().split())
    cal += cost * vol
if result == cal:
    print('Yes')
else:
    print('No')
n = int(input())
for i in range(1, n+1):
    a, b = map(int, input().split())
    print('Case #', i ,': ', a + b, sep='')
h, m = map(int, input().split())
t = int(input())

temp = 60 * h + m + t
h = temp // 60
m = temp % 60
if h >= 24:
    h -= 24
print(h, m)
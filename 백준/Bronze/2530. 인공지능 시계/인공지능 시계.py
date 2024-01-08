import sys
read = sys.stdin.readline

now_h, now_m, now_s = map(int, read().split())
t = int(read())

temp_h = t // 3600
t %= 3600
temp_m = t // 60
t %= 60
temp_s = t

over = 0
s = now_s + temp_s
if s >= 60:
    s -= 60
    over = 1
m = now_m + temp_m + over
over = 0
if m >= 60:
    m -= 60
    over = 1
h = now_h + temp_h + over
h %= 24

print(f'{h} {m} {s}')
h, m = map(int, input().split())
convert = 60 * h + m - 45
if convert < 0:
    convert = 60 * 24 + convert
print(convert // 60, convert % 60)
import math
day = int(input())
a = float(input())
b = float(input())
a = math.ceil(a / float(input()))
b = math.ceil(b / float(input()))
print(day - int(max(a, b)))
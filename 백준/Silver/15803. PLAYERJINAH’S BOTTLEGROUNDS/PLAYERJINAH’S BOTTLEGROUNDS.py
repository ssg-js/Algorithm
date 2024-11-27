import sys
read = sys.stdin.readline

x1, y1 = map(int, read().split())
x2, y2 = map(int, read().split())
x3, y3 = map(int, read().split())

if x1 == x2:
    if x3 == x1:
        print('WHERE IS MY CHICKEN?')
    else:
        print('WINNER WINNER CHICKEN DINNER!')
else:
    a = (y1-y2) / (x1-x2)
    b = y1 - a * x1
    
    v = a * x3 - y3 + b
    if v == 0:
        print('WHERE IS MY CHICKEN?')
    else:
        print('WINNER WINNER CHICKEN DINNER!')
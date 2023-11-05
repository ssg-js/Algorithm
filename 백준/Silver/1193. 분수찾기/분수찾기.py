import sys
n = int(sys.stdin.readline())
plus = 0
basic = 0
while plus < n:
    basic += 1
    plus += basic
if basic % 2 == 0:
    print(f'{basic-(plus-n)}/{plus-n+1}')
else:
    print(f'{plus-n+1}/{basic-(plus-n)}')
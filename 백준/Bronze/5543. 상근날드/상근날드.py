import sys
read = sys.stdin.readline

burger = [int(read()) for _ in range(3)]
soda = [int(read()) for _ in range(2)]
burger.sort()
soda.sort()
print(burger[0]+soda[0]-50)
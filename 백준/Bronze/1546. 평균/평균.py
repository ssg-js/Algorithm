import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
m = max(numbers)
print(sum(map(lambda x: x / m * 100, numbers)) / n)
import sys
mem = [1, 1]


def factorial(n):
    if n < len(mem):
        return mem[n]
    if n == len(mem):
        mem.append(n * mem[n-1])
    return n * factorial(n-1)


for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    if n >= k:
        print(1)
    else:
        print(factorial(k) // factorial(n) // factorial(k-n))



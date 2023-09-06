n = int(input())
for t in range(n):
    a, s = input().split()
    for c in s:
        print(c * int(a), end='')
    print()
import sys
read = sys.stdin.readline

n = int(read())
if n == 1: print(0)
else:
    arr = [True] * (n+1)
    prime_num = []
    for i in range(2, n+1):
        if arr[i]:
            prime_num.append(i)
            for k in range(i, n+1, i):
                arr[k] = False

    l, r = 0, 0
    value = prime_num[l]
    ans = 0
    while l < len(prime_num) and r < len(prime_num):
        if value == n:
            ans += 1
            value -= prime_num[l]
            l += 1
        elif value < n:
            r += 1
            if r == len(prime_num): break
            value += prime_num[r]
        else:
            value -= prime_num[l]
            l += 1
    print(ans)

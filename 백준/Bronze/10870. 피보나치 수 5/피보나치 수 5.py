def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


N = int(input())
ans = fibonacci(N)

print(ans)
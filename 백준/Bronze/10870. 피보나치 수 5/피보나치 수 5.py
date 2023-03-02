
def fibonacci(n):
    if n in store.keys():
        return store[n]
    if n < 2:
        return n
    store[n] = fibonacci(n-2) + fibonacci(n-1)
    return store[n]


N = int(input())
store = {}
ans = fibonacci(N)

print(ans)

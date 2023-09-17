n = int(input())
for i in range(n):
    for k in range(n-i-2, -1, -1):
        print(' ',end='')
    print('*' * (2*i+1))
for i in range(n-2, -1, -1):
    for k in range(n-i-2, -1, -1):
        print(' ',end='')
    print('*' * (2*i+1))
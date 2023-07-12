ans = []
for t in range(int(input())):
    a, b = map(int, input().split())
    a = a % 10
    if a == 1 or a == 5 or a == 6:
        ans.append(a)
    elif a == 0:
        ans.append(10)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        b = (b - 1) % 4 + 1
        ans.append((a ** b) % 10)
    else:  # 4 9
        b = (b - 1) % 2 + 1
        ans.append((a ** b) % 10)

print(*ans, sep='\n')

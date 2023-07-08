N = int(input())
F = int(input())

new_number = N - (N % 100)
ans = ""
for i in range(F):
    if (new_number + i) % F == 0:
        ans = str(i)
        break
        
if len(ans) == 2:
    print(ans)
else:
    print("0" + ans)

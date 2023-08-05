info = list(map(int, input().split()))
m = 0
for i in info:
    if info.count(i) == 2:
        print(1000+i*100)
        break
    elif info.count(i) == 3:
        print(10000+i*1000)
        break
    if i > m:
        m = i
else:
    print(m*100)
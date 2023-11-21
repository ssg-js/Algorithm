import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
acc = [0] * len(a)
for i in range(len(b)):
    value = 0
    for j in range(len(a)):
        if value < acc[j]:
            value = acc[j]
        elif b[i] == a[j]:
            acc[j] = value + 1
            
print(max(acc))

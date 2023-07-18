# 1430 - 1530

num = int(input())

result = 1
for a in range(2, num + 1):
    result = result * a

result = str(result)
for i in range(len(result) - 1, -1, -1):
    if result[i] != '0':
        print(result[i])
        break
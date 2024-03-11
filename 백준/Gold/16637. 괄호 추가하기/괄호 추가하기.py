import sys
read = sys.stdin.readline
n = int(read())
s = read().rstrip()
numbers = [s[i] for i in range(0, len(s), 2)]
operators = [s[i] for i in range(1, len(s), 2)]


def calculate(x, op, y):
    if op == '+':
        return int(x) + int(y)
    elif op == '-':
        return int(x) - int(y)
    elif op == '*':
        return int(x) * int(y)


stack = [(0, [])]
ans = -(2 ** 31)
while stack:
    idx, arr = stack.pop()
    if idx >= len(operators):
        cal_stack = [numbers[0]]
        for i in range(len(operators)):
            if i in arr:
                num = cal_stack.pop()
                cal_stack.append(calculate(num, operators[i], numbers[i+1]))
            else:
                cal_stack.append(operators[i])
                cal_stack.append(numbers[i+1])
        value = int(cal_stack[0])
        for i in range(1, len(cal_stack), 2):
            value = calculate(value, cal_stack[i], cal_stack[i+1])
        if value > ans:
            ans = value
        continue
    stack.append((idx + 1, arr[:])) # 안고름
    arr.append(idx)
    stack.append((idx + 2, arr[:])) # 고름
print(ans)


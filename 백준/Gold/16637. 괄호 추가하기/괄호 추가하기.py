import sys
read = sys.stdin.readline
n = int(read())
s = read().rstrip()


def calculate(x, op, y):
    if op == '+':
        return int(x) + int(y)
    elif op == '-':
        return int(x) - int(y)
    elif op == '*':
        return int(x) * int(y)


stack = [(0, int(s[0]))]
ans = -(2 ** 31)
while stack:
    idx, v = stack.pop()
    if idx == n - 1:
        if ans < v:
            ans = v
        continue
    if idx + 2 < n:
        stack.append((idx+2, calculate(v, s[idx+1], s[idx+2])))
    if idx + 4 < n:
        tmp = calculate(s[idx+2], s[idx+3], s[idx+4])
        stack.append((idx+4, calculate(v, s[idx+1], tmp)))
print(ans)


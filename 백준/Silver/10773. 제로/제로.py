stack = []
for k in range(1, int(input()) + 1):
    num = int(input())
    # 0을 만나면 pop
    if num == 0:
        stack.pop()
    # 0이 아니면 추가
    else:
        stack.append(num)

print(sum(stack))
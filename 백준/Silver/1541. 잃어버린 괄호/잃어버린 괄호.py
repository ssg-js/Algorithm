info = input()

plus = info.split('+')
nums = []
operator = []
for p in plus:
    # - 가 있으면 분리
    minus = p.split('-')
    if len(minus) >= 2:
        for m in minus:
            nums.append(int(m))
            operator.append('-')
        operator.pop()
    else:
        nums.append(int(minus[0]))
    operator.append('+')
operator.pop()


# - 뒤에 연속된 + 들을 묶어서 계산
def start():
    to_cal = []
    a = nums.pop()
    while operator:
        op = operator.pop()
        if op == '+':
            b = nums.pop()
            a = a + b
        elif op == '-':
            to_cal.append(a)
            a = nums.pop()
    to_cal.append(a)
    result = to_cal.pop()
    while to_cal:
        minus_num = to_cal.pop()
        result -= minus_num
    return result


print(start())
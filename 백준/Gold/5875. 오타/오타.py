import sys
read = sys.stdin.readline

s = read().rstrip()
arr = [0] * len(s)
for i in range(len(s)):
    if s[i] == '(':
        arr[i] = 1
    else:
        arr[i] = -1
hap = sum(arr)
cnt = 0
imos = []
if hap == -2: # 닫는 괄호가 하나 더 많음
    imos.append(arr[0])
    for i in range(1, len(arr)):
        imos.append(imos[i-1]+arr[i])
        if arr[i] == -1:
            cnt += 1
        if imos[i] == -1: # 닫는 괄호가 더 많아지는 부분
            break
elif hap == 2: # 여는 괄호가 하나 더 많음
    imos.append(arr[-1])
    for i in range(1, len(arr)):
        imos.append(imos[i-1]+arr[-1-i]) # arr 거꾸로 누적합
        if arr[-1-i] == 1:
            cnt += 1
        if imos[i] == 1: # 여는 괄호가 많아지는 부분(뒤에서 출발하는 시점에서 보면 닫는 괄호가 많아지는 부분)
            break
print(cnt)
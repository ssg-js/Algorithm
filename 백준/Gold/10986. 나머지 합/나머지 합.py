import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [*map(int, read().split())]
s = [0] * n
rest = [0] * n # 합에 m으로 나눈 나머지를 구함
ans = 0
info = [0] * m # 각 나머지를 가지는 갯수
for i in range(n):
    if i == 0:
        s[i] = arr[0]
    else:
        s[i] = s[i-1] + arr[i]
    rest[i] = s[i] % m
    if rest[i] == 0: # 0~i 까지 m으로 나눠지면 저장
        ans += 1
    info[rest[i]] += 1
for k in info: # k개 중에 2개 골라서 구간 만드는 경우의 수 => kC2
    ans += k*(k-1)//2
print(ans)

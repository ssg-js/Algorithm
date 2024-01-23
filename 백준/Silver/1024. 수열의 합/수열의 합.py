import sys
read = sys.stdin.readline

n, m = map(int, read().split())
# l(m->100)이 홀수면 l*k = n, 짝수면 l*k + l//2 = n을 찾으면 됨 -> l을 하나씩 증가시킴
# l이 홀수면 처음 수는 k - l//2, 짝수면 처음 수는 k - (l-1)//2
# l > 100이거나 l(l+1)//2 > n이면 -1 출력
ans = -1 # 시작 지점이거나 -1
for l in range(m, 101):
    if l * (l-1)//2 > n:
        break
    # l이 홀수
    if l % 2 == 1:
        if n % l == 0:
            ans = (n // l) - (l // 2)
            break
    # l이 짝수
    elif l % 2 == 0:
        if (n - l//2) % l == 0:
            ans = ((n - l//2) // l) - ((l - 1) // 2)
            break
# 답 출력
if ans == -1:
    print(ans)
else:
    for p in range(l):
        print(ans+p, end=' ')
        
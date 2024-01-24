import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = []
# 12345 => a = [1, 2, 3, 4, 5], b = [] => b.append(a.pop()) 로 만들기
# b[-1] > a.pop()(= a_temp)이면 b의 원소중 a_temp보다 큰 원소를 a에 append 후 a_temp를 b에 넣어서 내림차순정렬 후 끝
# b[-1] < a.pop()이면 b.append(a_temp)
# a가 내림차순인 경우 -1인데, 이건 처음에 원소별로 비교하면서 판별
ans = 0
for i in range(1, n):
    if a[i - 1] < a[i]:
        break
else:  # 내림차순인경우
    ans = -1
    print(ans)

if ans == 0:  # 마지막 순열이 아닌경우
    b.append(a.pop())
    while a:
        a_temp = a.pop()
        if b[-1] > a_temp:  # 이 조건을 만족할 때까지 반복
            # a_temp 보다 큰 b의 가장 작은 원소구하기
            v = n + 1
            idx = 0
            for i in range(len(b)):
                if b[i] > a_temp:
                    if b[i] < v:
                        v = b[i]
                        idx = i
            a.append(b.pop(idx))
            b.append(a_temp)
            b.sort(reverse=True)
            break
        else:  # b[-1] < temp
            b.append(a_temp)
    # 답 출력
    print(*a, end=' ')
    while b:
        print(b.pop(), end=' ')

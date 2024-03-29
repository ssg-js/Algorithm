import sys
read = sys.stdin.readline
num, check_num = map(int, read().split())
temperature = list(map(int, read().split()))
start, end = 0, check_num
v = sum(temperature[start:end]) # v: 이전 값들을 저장
ans = v
while end <= num:
    if v > ans: # 검사
        ans = v
    # 구간 이동
    if end < num:
        v -= temperature[start]
        v += temperature[end]
    start += 1
    end += 1
print(ans)
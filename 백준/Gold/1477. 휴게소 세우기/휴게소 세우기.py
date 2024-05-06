import sys
read = sys.stdin.readline
n, m, l = map(int, read().split())
rest = list(map(int, read().split()))
rest.sort()
left, right = 1, l
ans = l
while left <= right:
    tmp = 0 # 추가할 휴게소 수
    mid = (left + right) // 2
    nv = mid # 다음 휴게소가 있어야할 최대위치
    for v in rest:
        if nv >= v: # v가 적정 위치인 경우
            nv = v+mid
        else: # v가 현재 설정된 mid보다 먼경우
            cal = (v-nv) // mid
            if (v-nv) % mid > 0:
                cal += 1
            tmp += cal
            nv = v+mid
    if nv < l: # 마지막 휴게소부터 끝구간 처리
        cal = (l - nv) // mid
        if (l - nv) % mid > 0:
            cal += 1
        tmp += cal
    if tmp <= m: # mid 구간으로 여유롭게 휴게소 지음
        ans = min(ans, mid)
        right = mid-1
    else:
        left = mid+1
print(ans)





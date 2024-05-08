# 57분
import sys
read = sys.stdin.readline
n = int(read())
arr = [*map(int, read().split())]
arr.sort()
# 음수부터 0까지 하나 고르고 뒤에 idx부터 나머지 둘을 투포인터로 고르기 O(n^2)
ans = 0
for idx in range(n):
    # 첫번째 실력 고름
    cur = arr[idx]
    if cur > 0: # 첫번째 값이 양수면 0 못 만듬
        break
    # 나머지 둘 고르기
    target = -cur
    left, right = idx+1, n-1
    while left < right:
        # left 값이 이미 target을 넘어선 경우 종료
        if arr[left] > target:
            break
        value = arr[left] + arr[right]
        if value == target:
            if arr[left] == arr[right]: # 중복파티 nC2
                ans += (right-left+1) * (right-left) // 2
                break
            # left, right 각자 중복구간을 고려
            # left
            l_cnt = 1
            tmp_left = left + 1
            compare = arr[left]
            while compare == arr[tmp_left]:
                l_cnt += 1
                tmp_left += 1
            if l_cnt > 1:
                left = tmp_left
            else:
                left += 1
            # right
            r_cnt = 1
            tmp_right = right - 1
            compare = arr[right]
            while compare == arr[tmp_right]:
                r_cnt += 1
                tmp_right -= 1
            if r_cnt > 1:
                right = tmp_right
            else:
                right -= 1
            ans += l_cnt * r_cnt
        elif value < target: # 모자람
            left += 1
        else: # 넘침
            right -= 1
print(ans)

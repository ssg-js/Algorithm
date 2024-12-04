import sys
read = sys.stdin.readline

n, x = map(int, read().split())
burgers = [0] * 51
patties = [0] * 51
burgers[0] = 1
patties[0] = 1
for i in range(1, 51):
    burgers[i] = 3 + 2 * burgers[i-1]
    patties[i] = 1 + 2 * patties[i-1]

# 반씩 쪼개기
ans = 0
curL = n
target = x-1

while curL >= 0:
    if target == burgers[curL] - 1:
        ans += patties[curL]
        break
    if target == 0 and curL != 0:
        break   
    if curL == 0:
        ans += 1
        break

    mid = (burgers[curL]) // 2
    if target == mid:
        ans += patties[curL-1] + 1
        break
    elif target > mid:
        ans += patties[curL-1] + 1
        target = target - mid - 1
        curL -= 1
    else: # target < mid
        target -= 1
        curL -= 1

print(ans)
import sys
read = sys.stdin.readline
n, c = map(int, read().split())
house = [int(read()) for _ in range(n)]
house.sort()
left, right = 1, max(house) // (c-1)
ans = left
while left <= right:
    total = 0
    mid = (left + right) // 2
    nv = 0 # 다음 와이파이 설치하는 집 좌표의 최솟값
    for v in house:
        if v >= nv:
            total += 1
            nv = v + mid
    if total >= c:
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid-1
print(ans)
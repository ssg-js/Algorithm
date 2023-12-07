import sys
read = sys.stdin.readline

n = int(read())
building = list(map(int, read().split()))
ans = 0

for idx, start in enumerate(building):
    result = 0
    sight = [-1000000000, -1000000000]
    d = 1
    while idx-d >= 0 or idx+d < len(building):
        # 왼쪽
        if idx-d >= 0:
            if (building[idx-d]-start) / d > sight[0]:
                result += 1
                sight[0] = (building[idx-d]-start) / d
        # 오른쪽
        if idx+d < len(building):
            if (building[idx+d]-start) / d > sight[1]:
                result += 1
                sight[1] = (building[idx+d]-start) / d
        d += 1
    ans = max(ans, result)
print(ans)
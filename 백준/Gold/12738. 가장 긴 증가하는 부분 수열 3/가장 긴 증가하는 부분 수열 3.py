import sys
N = int(sys.stdin.readline())
original = list(map(int, sys.stdin.readline().split()))
LIS = []


def lower_bound(v, end, start=0): # 인덱스 값 반환a
    if start == end:
        return start
    middle = (start + end) // 2
    if v == LIS[middle]:
        return middle
    elif v > LIS[middle]:
        start = middle + 1
    else:
        end = middle
    return lower_bound(v, end, start)


for num in original:
    if len(LIS) == 0:
        LIS.append(num)
        continue
    if num > LIS[-1]:
        LIS.append(num)
    elif num < LIS[-1]:
        LIS[lower_bound(num, len(LIS) - 1)] = num

print(len(LIS))


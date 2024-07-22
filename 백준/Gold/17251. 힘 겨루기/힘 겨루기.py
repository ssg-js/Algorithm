import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
left_max = [0] * n
right_max = [0] * n
left_max[0] = arr[0]
right_max[n-1] = arr[n-1]

for i in range(1, n):
    left_max[i] = max(left_max[i-1], arr[i])
    right_max[n-1-i] = max(right_max[n-i], arr[n-1-i])

red_cnt = 0
blue_cnt = 0
for i in range(n-1):
    if left_max[i] > right_max[i+1]:
        red_cnt += 1
    elif left_max[i] < right_max[i+1]:
        blue_cnt += 1

if red_cnt > blue_cnt:
    print('R')
elif red_cnt < blue_cnt:
    print('B')
else:
    print('X')

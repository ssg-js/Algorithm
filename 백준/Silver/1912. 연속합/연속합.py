import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

for i in range(1, n):
    nums[i] = max(nums[i], nums[i] + nums[i-1])

print(max(nums))
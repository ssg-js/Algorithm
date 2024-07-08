import sys
read = sys.stdin.readline

n, k = map(int, read().split())
max_value = 0
arr = []
for _ in range(n):
    s, e = map(int, read().split())
    arr.append((s, e))
    max_value = max(max_value, e)
prefix_sum = [0] * (max_value + 2)
for s, e in arr:
    prefix_sum[s+1] += 1
    prefix_sum[e+1] -= 1

for i in range(1, len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]

for i in range(1, len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]

left, right = 0, 1
satisfied = False
while left <= right < len(prefix_sum)-1:
    value = prefix_sum[right] - prefix_sum[left]
    if value < k:
        right += 1
        continue
    elif value > k:
        left += 1
        continue
    satisfied = True
    break

if satisfied:
    print(left, right)
else:
    print(0, 0)
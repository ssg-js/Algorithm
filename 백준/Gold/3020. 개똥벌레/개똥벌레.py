import sys
read = sys.stdin.readline

n, h = map(int, read().split())
up = False
prefix_sum = [0] * h
for _ in range(n): # O(n)
    obs = int(read())
    if up:
        prefix_sum[-obs] += 1
    else:
        prefix_sum[0] += 1
        prefix_sum[obs] -= 1
    up = not up
for i in range(1, h): # O(h)
    prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]

obs_cnt, num = n, 0
for v in prefix_sum: # O(h)
    if v < obs_cnt:
        obs_cnt = v
        num = 1
        continue
    if v == obs_cnt:
        num += 1
        continue
print(obs_cnt, num)
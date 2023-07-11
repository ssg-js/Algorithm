H, W = map(int, input().split())
block = list(map(int, input().split()))
ans = 0

for i in range(1, W - 1):
    before = max(block[:i])
    after = max(block[i+1:])
    compare = min(before, after)
    if block[i] < compare:
        ans += compare - block[i]

print(ans)


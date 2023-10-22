import sys
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
up, down = [], []
big = 0
for i in range(N):
    # 커지는 경우
    if not up:
        up.append(data[i])
    else:
        if up[-1] <= data[i]:
            up.append(data[i])
        else:
            big = max(big, len(up))
            up = [data[i]]
    # 작아지는 경우
    if not down:
        down.append(data[i])
    else:
        if down[-1] >= data[i]:
            down.append(data[i])
        else:
            big = max(big, len(down))
            down = [data[i]]

print(max(len(up), len(down), big))



N, K = map(int, input().split())
kit = list(map(int, input().split()))
ans = 0


def cnt(now, day, used):
    global K, ans
    if day == 0:
        ans += 1
        return
    for i in range(len(kit)):
        if i not in used:
            if now - K + kit[i] >= 500:
                used.append(i)
                cnt(now - K + kit[i], day - 1, used)
                used.pop()


cnt(500, N, [])
print(ans)
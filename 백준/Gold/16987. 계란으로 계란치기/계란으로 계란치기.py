import sys
read = sys.stdin.readline

n = int(read())
arr = [list(map(int, read().split())) for _ in range(n)]
ans = 0

def solve(idx, states, cnt):
    global ans
    if ans == len(states):
        return
    if idx == len(states):
        ans = max(cnt, ans)
        return

    s, w = states[idx]
    if s <= 0:
        solve(idx+1, states, cnt)
        return
    
    for i in range(len(states)):
        if idx == i: continue

        temp = states[:]
        ns, nw = temp[i]
        if ns <= 0:
            solve(idx+1, temp[:], cnt)
            continue
        temp[idx] = [s-nw, w]
        temp[i] = [ns-w, nw]
        nCnt = cnt
        if s-nw <= 0: nCnt += 1
        if ns-w <= 0: nCnt += 1
        solve(idx+1, temp, nCnt)

solve(0, arr, 0)
print(ans)
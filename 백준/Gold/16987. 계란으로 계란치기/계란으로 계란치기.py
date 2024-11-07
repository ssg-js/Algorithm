import sys
read = sys.stdin.readline

n = int(read())
arr = [list(map(int, read().split())) for _ in range(n)]
ans = 0

def solve(idx, states):
    global ans
    if idx == len(states):
        cnt = 0
        for s, w in states:
            if s <= 0: cnt += 1
        ans = max(cnt, ans)
        return

    s, w = states[idx]
    if s <= 0:
        solve(idx+1, states)
        return
    
    for i in range(len(states)):
        if idx == i: continue

        temp = states[:]
        ns, nw = temp[i]
        if ns <= 0:
            solve(idx+1, temp[:])
            continue
        temp[idx] = [s-nw, w]
        temp[i] = [ns-w, nw]
        solve(idx+1, temp)

solve(0, arr)
print(ans)
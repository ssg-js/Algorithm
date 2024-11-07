import sys
read = sys.stdin.readline

n = int(read())
arr = [list(map(int, read().split())) for _ in range(n)]
ans = 0

def solve(idx, cnt):
    global ans
    if ans == len(arr):
        return
    if idx == len(arr):
        ans = max(cnt, ans)
        return

    s, w = arr[idx]
    if s <= 0:
        solve(idx+1, cnt)
        return
    
    flag = False
    for i in range(len(arr)):
        if idx == i: continue

        ns, nw = arr[i]
        if ns <= 0:
            continue
        flag = True
        arr[idx] = [s-nw, w]
        arr[i] = [ns-w, nw]
        nCnt = cnt
        if s-nw <= 0: nCnt += 1
        if ns-w <= 0: nCnt += 1
        solve(idx+1, nCnt)
        arr[idx] = [s, w]
        arr[i] = [ns, nw]
    if not flag:
        solve(idx+1, cnt)
    

solve(0, 0)
print(ans)
import sys
read = sys.stdin.readline
n = int(read())
info = [[*map(int, read().split())][1:] for _ in range(n)]
visited = [[False] * 10 for _ in range(n+1)] # 전날 어떤 떡 줬는지
done = False


def dfs(idx, arr): # 순서, 현재까지 떡 현황
    global done
    if done:
        return
    if idx == n:
        print(*arr, sep="\n")
        done = True
        return
    for rice_cake in info[idx]:
        if not visited[idx+1][rice_cake] and rice_cake != arr[-1]: # 이전이랑 다른 종류 떡
            visited[idx+1][rice_cake] = True
            dfs(idx+1, arr+[rice_cake])


for cake in info[0]:
    if done:
        break
    visited[1][cake] = True
    dfs(1, [cake])
if not done:
    print(-1)


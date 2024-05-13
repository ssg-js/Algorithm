import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [*map(lambda x:[int(x)]*3, read().split())] # 이전 방향별 최솟값
delta = [1, 0, -1]
INF = 100 * 1000
for _ in range(n-1):
    info_arr = [*map(int, read().split())]
    n_arr = []
    # 1. 위치정하기
    # 2. 이전방향정하기
    # 3. 이전방향에서 방향이 겹치지 않는 방향의 값의 최솟값 들고오기
    for i in range(m): # 1
        temp_arr = [INF, INF, INF]
        for d in range(3): # 2, arr에 저장할 이전 방향 (아래idx - 위idx)
            if 0 <= i-delta[d] < m: # 값 가져올 위idx 검사
                for before_d in range(3):
                    if d != before_d: # 3
                        temp_arr[d] = min(temp_arr[d], arr[i-delta[d]][before_d]+info_arr[i])
        n_arr.append(temp_arr)
    arr = n_arr
ans = INF
for a in arr:
    ans = min(ans, *a)
print(ans)


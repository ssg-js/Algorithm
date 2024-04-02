import sys
read = sys.stdin.readline
n, sushi_num, k, coupon = map(int, read().split())
plates = []
state = dict() # 해당 구간 내 초밥별 몇개 있는지
for _ in range(n):
    p = int(read())
    plates.append(p)
    if p not in state.keys():
        state[p] = 0
ans = 0
start, end = 0, k-1
state[coupon] = 1 # 쿠폰 먼저 1처리
cnt = 1
for i in range(start, end+1): # 처음 구간 처리
    if state[plates[i]] == 0: # 한번만 세기
        cnt += 1
    state[plates[i]] += 1
ans = cnt
while start < n:
    # 구간 이동하면서 왼쪽 끝 제거
    if state[plates[start]] > 0:
        state[plates[start]] -= 1
        if state[plates[start]] == 0: # 아예 없으면 빼기
            cnt -= 1
    start += 1
    # 오른쪽 끝 추가
    end = (end + 1) % n
    if state[plates[end]] == 0: # 처음 추가할 때만 세기
        cnt += 1
    state[plates[end]] += 1
    if ans < cnt:
        ans = cnt
print(ans)

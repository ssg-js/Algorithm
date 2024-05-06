import sys
read = sys.stdin.readline
n, k = map(int, read().split())
board = [int(read()) for _ in range(n)] # 각 심사대 대기 시간
left, right = min(board), max(board) * k # 정답 시간을 이분탐색으로 도출
ans = right
while left <= right:
    total = 0
    mid = (left + right) // 2
    for t in board:
        total += mid // t # 정답 추정시간(mid)에 각 대기시간을 나눠 몇명까지 통과하는지 total에 저장
    if total >= k: # 모든 사람이 충분히 통과할수 있는 시간이면
        right = mid - 1
        ans = min(ans, mid)
    else: # 통과못하면 시간이 부족하므로
        left = mid + 1
print(ans)



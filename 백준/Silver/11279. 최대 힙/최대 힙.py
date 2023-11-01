# [BOJ] 11279. 최대 힙
# 소요 시간 : 60분

from heapq import heappush, heappop
import sys

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    # 숫자 출력
    if num == 0:
        # heap 이 비어 있으면
        if len(heap) == 0:
            print(0)
        # heap 이 차 있으면 최댓값 출력
        else:
            print(-heappop(heap))
    # 배열에 숫자 추가
    else:
        heappush(heap, -num)


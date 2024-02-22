import sys
from heapq import heappush, heappop
read = sys.stdin.readline
v, e = map(int, read().split())
heap = []
parent = [i for i in range(v+1)] # 싸이클 검사할 테이블
for _ in range(e): # 간선 비용 최소부터 처리하도록 heap 사용
    a, b, w = map(int, read().split())
    heappush(heap, (w, a, b))
ans = 0
    
    
def get_parent(arr, x):
    if arr[x] == x:
        return x
    else:
        return get_parent(arr, arr[x])
        
        
def union_parent(arr, x, y): # 부모 합치기
    x_parent = get_parent(arr, x)
    y_parent = get_parent(arr, y)
    if x_parent < y_parent:
        arr[y_parent] = x_parent
    else:
        arr[x_parent] = y_parent
        
        
def find(arr, x, y): # 부모 같은지 확인
    x_parent = get_parent(arr, x)
    y_parent = get_parent(arr, y)
    if x_parent == y_parent:
        return True
    else:
        return False
    
    
while heap: # 간선 비용 최소로 스패딩 트리 만들기
    w, a, b = heappop(heap)
    if find(parent, a, b): # 싸이클 있는 경우
        continue
    union_parent(parent, a, b)
    ans += w
print(ans)
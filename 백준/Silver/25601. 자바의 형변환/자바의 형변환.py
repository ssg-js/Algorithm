# [BOJ] 25601. 자바의 형변환
# 소요 시간 : 20분
from collections import deque

n = int(input())
rel = dict()
ans = 0
for i in range(n - 1):
    child, parent = input().split()
    rel[child] = parent # 부모는 무조건 하나

one, two = input().split()
a = one
while a and ans == 0:
    a = rel.get(a, '')
    if a == two:
        ans = 1
b = two
while b and ans == 0:
    b = rel.get(b, '')
    if b == one:
        ans = 1
print(ans)
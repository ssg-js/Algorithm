import sys
people_num, party_num = map(int, sys.stdin.readline().split())
root = [i for i in range(people_num+1)]
info = list(map(int, sys.stdin.readline().split()))
parties = []
if info[0] > 0:
    for p in info[1:]:
        root[p] = 0


def find(x):
    if root[x] == x:
        return x
    else:
        return find(root[x])


# root에 0이 나오면 다 갱신
def union(arr):
    global root
    ra = []
    for i in range(len(arr)):
        ra.append(find(arr[i]))
    rv = min(ra)
    for n in ra:
        root[n] = rv


# 관계 형성
for _ in range(party_num):
    temp = list(map(int, sys.stdin.readline().split()))
    parties.append((temp[1:]))
    union(temp[1:])
# 안전한 파티 확인
ans = 0
safe = True
for a in parties:
    safe = True
    for aa in a:
        if find(aa) == 0:
            safe = False
            break
    if safe:
        ans += 1
print(ans)
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
edge = [[] for _ in range(n+1)] # 건물 관계, 앞서 지어져야하는 건물의 정보를 담고있음
built = [0] * (n+1) # 건물 지어졌는지(중복가능)
# 1번 건물은 언제든지 건설 가능
built[0] = 1
edge[1].append(0)
for _ in range(m):
    a, b = map(int, read().split())
    edge[b].append(a)
for _ in range(k):
    act, target = map(int, read().split())
    if act == 1: # 건설
        for b in edge[target]: # 여기서 시간초과날듯?
            if built[b] == 0: # target 앞선 건물 건설 안됨
                break
        else:
            built[target] += 1
            continue
        print("Lier!")
        break
    else: # 파괴
        if built[target] == 0: # 없는 건물 파괴
            print("Lier!")
            break
        built[target] -= 1
else:
    print("King-God-Emperor")

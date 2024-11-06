import sys
from collections import deque
read = sys.stdin.readline

arr = []
for i in range(3):
    a = read().split()
    if len(a) == 1:
        arr.append('')
    else:
        arr.append(a[1])
queue = deque()
queue.append(arr)
cnt = 0
visited = dict()
visited['0'+str(arr[0])+'1'+str(arr[1])+'2'+str(arr[2])] = True

def check(arr):
    for i in range(len(arr[0])):
        if arr[0][i] != 'A': return False
    for i in range(len(arr[1])):
        if arr[1][i] != 'B': return False
    for i in range(len(arr[2])):
        if arr[2][i] != 'C': return False
    return True

if check(arr):
    print(0)
else:
    flag = False
    while queue:
        if flag: break
        for _ in range(len(queue)):
            if flag: break
            state = queue.popleft()

            for i, s in enumerate(state):
                if flag: break
                if len(s) == 0: continue

                c = s[-1]
                for k in range(3):
                    if i == k: continue
                    temp = state[:]
                    temp[i] = s[:-1]
                    temp[k] += c
                    if '0'+str(temp[0])+'1'+str(temp[1])+'2'+str(temp[2]) in visited.keys(): continue

                    visited['0'+str(temp[0])+'1'+str(temp[1])+'2'+str(temp[2])] = True
                    queue.append(temp)

                    if (check(temp)):
                        flag = True
                        break
        cnt += 1

    print(cnt)



import sys
from collections import deque


def cal(command, s):
    if command == 'D':
        return 2*int(s) % 10000
    elif command == 'S':
        tmp = int(s) - 1
        if tmp < 0:
            tmp = 9999
        return tmp
    elif command == 'L':
        tmp = '0' * (4-len(str(s))) + str(s)
        return int(tmp[1:] + tmp[0])
    elif command == 'R':
        tmp = '0' * (4-len(str(s))) + str(s)
        return int(tmp[3] + tmp[:3])


read = sys.stdin.readline
for _ in range(int(read())):
    a, b = map(int, read().split())
    action = ['D', 'S', 'L', 'R']
    visited = set()
    queue = deque()
    queue.append((a, ''))
    visited.add(a)
    ans = ''
    flag = True
    while queue and flag:
        for _ in range(len(queue)):
            cur, text = queue.popleft()
            if cur == b:
                ans = text
                flag = False
                break
            for act in action:
                tmp = cal(act, cur)
                if tmp not in visited:
                    visited.add(tmp)
                    queue.append((tmp, text+act))
    print(ans)
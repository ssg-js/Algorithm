from collections import deque
import sys

for t in range(int(input())):
    p = sys.stdin.readline().rstrip()
    end = len(p)
    idx = 0
    n = int(sys.stdin.readline())
    info = sys.stdin.readline().rstrip()
    if len(info) == 2:
        array = deque([])
    else:
        array = deque(map(int, info[1:len(info)-1].split(',')))
    is_flip = False
    is_err = False
    while idx != end and not is_err:
        if p[idx] == 'R':
            is_flip = not is_flip
        else:
            if array:
                if is_flip:
                    array.pop()
                else:
                    array.popleft()
            else:
                is_err = True
                break
        idx += 1

    if is_err:
        print('error')
    else:
        if is_flip:
            array.reverse()
        temp = '['
        for i, s in enumerate(array):
            temp = temp + str(s)
            if i < len(array) - 1:
                temp += ','
        temp = temp + ']'
        print(temp)
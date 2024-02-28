import sys
read = sys.stdin.readline
height, start, end, up, down = map(int, read().split())
visited = set()
visited.add(start)
cnt = 0
use_stair = 'use the stairs'
while True:
    if start == end:
        print(cnt)
        break
    if start < end:
        if up == 0:
            print(use_stair)
            break
        if start + up > height:
            if start - down < 1:
                print(use_stair)
                break
            start -= down + up
        start += up
    elif start > end:
        if down == 0:
            print(use_stair)
            break
        if start - down < 1:
            if start + up > height:
                print(use_stair)
                break
            start += up + down
        start -= down
    if start in visited:
        print(use_stair)
        break
    visited.add(start)
    cnt += 1

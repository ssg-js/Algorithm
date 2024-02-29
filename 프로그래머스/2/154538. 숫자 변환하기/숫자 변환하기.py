from collections import deque

def solution(x, y, n):
    answer = 0
    visited = set()
    queue = deque([y])
    visited.add(y)
    cnt = len(queue)
    impos = True
    while queue:
        now = queue.popleft()
        if now < x:
            continue
        if now == x:
            impos = False
            break
        if now % 3 == 0 and now // 3 >= x and now // 3 not in visited:
            queue.append(now // 3)
            visited.add(now // 3)
        if now % 2 == 0 and now // 2 >= x and now // 2 not in visited:
            queue.append(now // 2)
            visited.add(now // 2)
        if now - n >= x and now - n not in visited:
            queue.append(now - n)
            visited.add(now - n)
        cnt -= 1
        if cnt == 0:
            cnt = len(queue)
            answer += 1
    if impos:
        answer = -1
    return answer
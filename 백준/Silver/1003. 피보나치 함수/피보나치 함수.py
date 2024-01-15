import sys
read = sys.stdin.readline
result = [[1,0], [0,1], [1,1]]

for t in range(int(read())):
    n = int(read())
    if n == 0 or n == 1: # 0, 1인 케이스는 바로 처리
        print(*result[n])
        continue
    # 이외의 케이스
    for i in range(n+1):
        if i < len(result): # result에 값이 있는 경우 패스
            continue
        # result에 값이 없는 경우 추가
        result.append([result[i-1][0]+result[i-2][0], result[i-1][1]+result[i-2][1]])
    print(*result[n])
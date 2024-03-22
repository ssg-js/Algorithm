def solution(friends, gifts):
    answer = 0
    n = len(friends)
    info = [[0] * n for _ in range(n)]
    to_idx = dict()
    for i, f in enumerate(friends):
        to_idx[f] = i
    for pair in gifts:
        a, b = pair.split()
        info[to_idx[a]][to_idx[b]] += 1
    receive_table = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if (info[i][j] > 0 or info[j][i] > 0) and info[i][j] != info[j][i]:
                if info[i][j] > info[j][i]:
                    receive_table[i] += 1
                elif info[i][j] < info[j][i]:
                    receive_table[j] += 1
            else:
                i_point, j_point = 0, 0
                for k in range(n):
                    i_point += info[i][k]
                    i_point -= info[k][i]
                    j_point += info[j][k]
                    j_point -= info[k][j]
                if i_point > j_point:
                    receive_table[i] += 1
                elif i_point < j_point:
                    receive_table[j] += 1
    for v in receive_table:
        if v > answer:
            answer = v
    return answer
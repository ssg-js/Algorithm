def solution(n, arr1, arr2):
    whole_map = []
    for i in range(n):
        whole_map.append(int(arr1[i]) | int(arr2[i]))

    print(whole_map)
    answer = []
    for i in range(n):
        binary = bin(whole_map[i])[2:n+2]
        if len(binary) != n:
            binary = '0' * (n - len(binary)) + binary
        answer.append(binary.replace('1', '#').replace('0', ' '))

    return answer
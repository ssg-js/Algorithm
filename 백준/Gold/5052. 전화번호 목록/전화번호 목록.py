import sys
read = sys.stdin.readline
for _ in range(int(read())):
    n = int(read())
    phone_number = [read().rstrip() for _ in range(n)]
    hash_map = {}
    ans = 'YES'
    for number in phone_number:
        hash_map[number] = 1
    for number in phone_number:
        temp = ''
        for num in number:
            temp += num
            if temp in hash_map and temp != number:
                ans = 'NO'
    print(ans)
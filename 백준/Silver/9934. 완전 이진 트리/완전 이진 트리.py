'''
2
2 1 3

3
1 6 4 3 5 2 7
'''


def find_root(arr, depth):
    if depth == k:
        return
    mid = len(arr) // 2
    results[depth].append(arr[mid])
    depth += 1
    find_root(arr[:mid], depth)
    find_root(arr[mid+1:], depth)


k = int(input())
tree = list(map(int, input().split()))

results = [[] for _ in range(k)]
find_root(tree, 0)

for result in results:
    print(*result)



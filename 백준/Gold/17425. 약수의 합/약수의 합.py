import sys
read = sys.stdin.readline

t = int(read())
arr = []
max_value = 0
for _ in range(t): # t: 100,000
    arr.append(int(read()))
    if arr[-1] > max_value:
        max_value = arr[-1]

f_arr = [1] * (max_value + 1) # n: 1,000,000

for i in range(2, len(f_arr)): # i: 1,000,000
    for k in range(i, len(f_arr), i):
        f_arr[k] += i

for i in range(2, len(f_arr)): # i: 1,000,000
    f_arr[i] = f_arr[i] + f_arr[i-1]

for k in arr: # t: 100,000
    print(f_arr[k])
# boj 13458 시험감독

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

counter = 0

for i, num in enumerate(A):
    if (num - B) < 0:
        A[i] = 0
    else:
        A[i] = num - B
    counter += 1
    if A[i] > 0:
        if A[i] % C == 0:
            counter += A[i] // C
        else:
            counter += A[i]//C + 1

print(counter)

import sys
read = sys.stdin.readline
n, k = map(int, read().split())
ans = 0


def check(): # n의 2진수에서 1의 갯수가 k이하인지 체크
    cnt = 0
    for p in range(25): # 2^24 = 16,777,216
        if 2 ** p > n:
            break
        if n & (1 << p) == (1 << p): # 1 갯수 카운트
            cnt += 1
    if cnt <= k:
        return False
    else:
        return True


while check():
    ans += 1
    n += 1
print(ans)
import sys
read = sys.stdin.readline


def check(s):
    for width in range(2, len(s)+1):
        for start in range(len(s)-width-width+1):
            end = start+width
            if s[start:end] == s[start+width:end+width]:
                return True
    return False


def make(s=''):
    global ans
    if len(ans) > 0:
        return
    if check(s): # 나쁜 수열 체크
        return
    if len(s) == n: # 수열 완성
        ans = s
        return
    for p in ['1', '2', '3']:
        if len(s) > 0:
            if p == s[-1]: # 이전숫자랑 같은거로 안만듬
                continue
        make(s+p)


n = int(read())
ans = ''
make()
print(ans)


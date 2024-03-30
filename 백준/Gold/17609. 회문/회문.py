import sys
read = sys.stdin.readline


for _ in range(int(read())):
    s = read().rstrip()
    start, end = 0, len(s)-1
    palindrome = True # 회문 판정
    semi = False # 유사회문 판정
    while start < end:
        if s[start] == s[end]: # 같으면 지나가기
            start += 1
            end -= 1
            continue
        # 다를 경우
        palindrome = False
        if semi: # 이미 문자하나 삭제한 경우
            semi = False
            break
        else: # 유사회문 가능한지 검사
            semi = True
            if s[start+1] == s[end]:
                tmp_pal = True
                tmp_s, tmp_e = start+2, end-1
                while tmp_s < tmp_e:
                    if s[tmp_s] != s[tmp_e]:
                        tmp_pal = False
                    tmp_s += 1
                    tmp_e -= 1
                if tmp_pal:
                    break
            if s[start] == s[end-1]:
                tmp_pal = True
                tmp_s, tmp_e = start+1, end-2
                while tmp_s < tmp_e:
                    if s[tmp_s] != s[tmp_e]:
                        tmp_pal = False
                    tmp_s += 1
                    tmp_e -= 1
                if tmp_pal:
                    break
            # 불가능
            semi = False
            break
    if palindrome:
        print(0)
    elif semi:
        print(1)
    else:
        print(2)
            
    
            
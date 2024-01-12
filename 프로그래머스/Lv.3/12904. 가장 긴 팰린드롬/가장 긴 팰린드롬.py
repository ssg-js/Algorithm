def solution(s):
    answer = 0
    
    # 각 인덱스 중심으로 양쪽으로 퍼지며 검사 후 길이를 리턴
    def check(text, idx):
        # 홀수개
        front, back = idx, idx
        cnt_odd = 1
        end = False
        while not end:
            front -= 1
            back += 1
            if front >= 0 and back < len(text):
                if text[front] == text[back]:
                    cnt_odd += 2
                else:
                    end = True
            else:
                end = True
        # 짝수개
        front, back = idx, idx + 1
        cnt_even = 0
        end = False
        while not end:
            if front >= 0 and back < len(text):
                if text[front] == text[back]:
                    cnt_even += 2
                else:
                    end = True
            else:
                end = True    
            front -= 1
            back += 1
        return max(cnt_odd, cnt_even)
                
    for i in range(0,len(s)):
        answer = max(answer, check(s, i))

    return answer
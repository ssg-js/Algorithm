# 1159 ~ 1234

# 앞뒤로 pop 해서 수을 만든수 set에 저장후 중복 판별 후 개수 출력

number = input()
ans = 0


def count(result):
    global ans
    # 남은게 같은 문자면 중복되니깐 종료
    temp = set(list(result))
    if len(temp) == 1:
        ans += 1
        return
    else: # 아니면 계속 진행
        count(result[1:])
        count(result[:-1])


count(number)
print(ans)
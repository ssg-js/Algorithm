# 스위치 켜고 끄기

N = int(input())
switch_status = list(map(int, input().split()))                             # 스위치 상태
students = int(input())                                                     # 학생 수
for _ in range(students):
    gender, number = map(int, input().split())                              # 성별, 받은 번호
    if gender == 1:                                                         # 남자인 경우
        for k in range(number, N + 1):
            if k % number == 0:
                switch_status[k - 1] = (switch_status[k - 1] + 1) % 2       # 상태 바꾸기

    elif gender == 2:                                                       # 여자인 경우
        switch_status[number - 1] = (switch_status[number - 1] + 1) % 2     # 일단 해당 스위치 상태 바꾸기
        for k in range(1, min([number, N - number + 1])):                   # 양쪽으로 얼마나 갈지 정하기 -> 리스트 크기 벗어나지 않게
            a = switch_status[number - 1 - k]
            b = switch_status[number - 1 + k]
            if a == b:                                                      # 대칭인 경우
                changed = (a + 1) % 2
                switch_status[number - 1 - k], switch_status[number - 1 + k] = changed, changed
            else:
                break                                                       # 대칭 안되면 바로

while switch_status:
    print(*switch_status[:20])
    switch_status = switch_status[20:]





# month: i = 0 - 11
def payment(month, cost):
    if month >= 12:
        all_case.append(cost)
        return
    # 1일
    payment(month + 1, cost + plan[month] * price[0])
    # 1달
    payment(month + 1, cost + price[1])
    # 3달
    payment(month + 3, cost + price[2])
    # 1년
    if month == 0:
        payment(month + 12, cost + price[3])


for t in range(1, int(input()) + 1):
    # price: i = 0, 1, 2, 3
    price = list(map(int, input().split()))
    # plan: i = 0 - 11
    plan = list(map(int, input().split()))

    all_case = []
    payment(0, 0)

    answer = min(all_case)
    print(f'#{t} {answer}')



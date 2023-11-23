# 1. 가장 먼곳부터 처리
# 2. 갈때는 배달만, 올때는 수거만
# 3. 항상 최대치를 배달과 수거

def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = []
    pickup = []
    for i, v in enumerate(deliveries):
        if v > 0:
            deliver.append((i+1, v))
    for i, v in enumerate(pickups):
        if v > 0:
            pickup.append((i+1, v))
    while deliver or pickup:
        distance = 0
        # 배달
        temp = cap
        while deliver and temp > 0:
            d, v = deliver.pop()
            distance = max(d, distance)
            temp -= v
        if temp < 0:
            deliver.append((d, -temp))
        # 수거
        temp = cap
        while pickup and temp > 0:
            d, v = pickup.pop()
            distance = max(d, distance)
            temp -= v
        if temp < 0:
            pickup.append((d, -temp))
        # 거리 더하기
        answer += distance * 2
        
    return answer
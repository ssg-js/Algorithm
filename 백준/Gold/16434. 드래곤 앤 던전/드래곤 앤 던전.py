import sys
read = sys.stdin.readline
n, power = map(int, read().split())
room = [tuple(map(int, read().split())) for _ in range(n)]
left, right = 1, 1000000 * 1000000 * n
ans = right
while left <= right:
    max_hp = (left + right) // 2
    cur_hp = max_hp
    cur_power = power
    for t, a, h in room:
        if t == 1: # 몬스터
            # 용사 vs 몬스터를 while로 돌리면 시간초과
            turn_a = h // cur_power # 몬스터 죽이는 턴수
            if h % cur_power > 0:
                turn_a += 1
            turn_b = cur_hp // a # 용사 죽이는 턴수
            if cur_hp % a > 0:
                turn_b += 1
            value = min(turn_a, turn_b) # 둘중 하나가 죽을 때까지 공격 하거나 공격 받은 턴 수
            h -= cur_power * value
            if h <= 0: # 몬스터가 먼저 또는 동시에 죽음
                cur_hp -= a * (value-1)
                if cur_hp <= 0:
                    break
            else: # 용사가 먼저 죽음
                cur_hp -= a * value
            if cur_hp <= 0:
                break
        else: # 포션
            cur_power += a
            cur_hp = min(cur_hp+h, max_hp)
    if cur_hp <= 0: # 사망
        left = max_hp+1
    else: # hp 조건 충족함
        right = max_hp-1
        ans = min(max_hp, ans)
print(ans)




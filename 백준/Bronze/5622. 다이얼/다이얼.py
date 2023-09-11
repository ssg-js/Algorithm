s = input().rstrip()
ans = 0
start = ord('A')
for a in s:
    if start <= ord(a) < start + 3:
        ans += 3
    elif start + 3 <= ord(a) < start + 6:
        ans += 4
    elif start + 6 <= ord(a) < start + 9:
        ans += 5
    elif start + 9 <= ord(a) < start + 12:
        ans += 6
    elif start + 12 <= ord(a) < start + 15:
        ans += 7
    elif start + 15 <= ord(a) < start + 19:
        ans += 8
    elif start + 19 <= ord(a) < start + 22:
        ans += 9
    elif start + 22 <= ord(a) < start + 26:
        ans += 10
print(ans)
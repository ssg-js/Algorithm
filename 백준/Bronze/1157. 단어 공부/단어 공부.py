import sys

s = sys.stdin.readline().rstrip().upper()
checked = dict()
max_num = 0
for i in range(len(s)):
    if s[i] not in checked:
        checked[s[i]] = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                checked[s[i]] += 1
        max_num = max(max_num, checked[s[i]])

cnt = 0
ans = ''
for k, v in checked.items():
    if v == max_num:
        cnt += 1
        ans = k

if cnt > 1:
    print('?')
else:
    print(ans)

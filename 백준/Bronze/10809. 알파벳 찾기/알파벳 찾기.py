import sys
word = sys.stdin.readline().rstrip()
ans = []
origin = ord('a')
for i in range(26):
    letter = chr(i + origin)
    for j, c in enumerate(word):
        if letter == c:
            ans.append(j)
            break
    else:
        ans.append(-1)
print(*ans)
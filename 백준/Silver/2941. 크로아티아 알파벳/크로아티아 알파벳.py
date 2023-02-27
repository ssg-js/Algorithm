croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
cnt = 0
for alpha in croatia_alpha:
    cnt += word.count(alpha)
    word = word.replace(alpha, '0')

word = word.replace('0', '')
cnt += len(word)

print(cnt)
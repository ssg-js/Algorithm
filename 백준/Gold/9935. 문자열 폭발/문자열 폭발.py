# s.replace(a, b) 복잡도 : O(len(str) * (len(a) + len(b)/len(a)))
# 여기서는 1000000 * 36 = 36000000
# count 의 복잡도는 O(
# 복잡도 질문하기!
line = input()
word = input()

# # 틀린 거
# cnt = line.count(word)
#
# while cnt > 0:
#     line = line.replace(word, '')
#     cnt = line.count(word)
# 고친 거
stack = []
for i in range(len(line)):
    stack.append(line[i])
    if ''.join(stack[-len(word):]) == word:
        for _ in range(len(word)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
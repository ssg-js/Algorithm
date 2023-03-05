def solution(s):
    answer = 0
    num_words = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]
    for i, word in enumerate(num_words):
        s = s.replace(word, str(i))
    answer = int(s)
    return answer

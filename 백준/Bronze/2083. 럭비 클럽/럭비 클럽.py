import sys
read = sys.stdin.readline

while True:
    name, age, weight = read().split()
    if name == '#':
        break
    else:
        if int(age) > 17 or int(weight) >= 80:
            print(f'{name} Senior')
        else:
            print(f'{name} Junior')
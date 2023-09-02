import sys
for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    print(s[0] + s[-1])
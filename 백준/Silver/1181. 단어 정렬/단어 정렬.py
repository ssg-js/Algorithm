import sys
N = int(sys.stdin.readline())
ans = [sys.stdin.readline().rstrip() for _ in range(N)]
ans = list(set(ans))
ans.sort(key=lambda x:(len(x), x))
print(*ans, sep='\n')
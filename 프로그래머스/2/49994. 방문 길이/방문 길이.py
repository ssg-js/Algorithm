def solution(dirs):
    answer = 0
    delta = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    
    visited = [[{'U': False, 'D': False, 'R': False,  'L': False} for _ in range(11)] for _ in range(11)]
    x, y = 5, 5
    for d in dirs:
        dx, dy = delta[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < 11 and 0 <= ny < 11:
            if not visited[nx][ny][d]: 
                answer += 1
                visited[nx][ny][d] = True
                visited[x][y][reverse(d)] = True
            x, y = nx, ny
        else:
            continue            
    return answer

def reverse(c):
    if c == 'U': return 'D'
    if c == 'D': return 'U'
    if c == 'R': return 'L'
    if c == 'L': return 'R'
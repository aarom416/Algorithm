from collections import deque

def solution(maps):
    answer = 0
    
    queue = deque([(0,0)])
    m = len(maps)
    n = len(maps[0])
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    if maps[m-1][n-1] == 1:
        return -1
    return maps[m-1][n-1]
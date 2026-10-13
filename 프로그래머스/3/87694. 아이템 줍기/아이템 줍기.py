from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 좌표를 2배 확대
    SIZE = 102

    graph = [[0] * SIZE for _ in range(SIZE)]
    
    # 1. 사각형 전체를 1로 채우기
    for rect in rectangle:
        x1, y1, x2, y2 = rect

        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                graph[y][x] = 1

    # 2. 사각형 내부를 0으로 만들기
    # → 테두리만 1로 남김
    for rect in rectangle:
        x1, y1, x2, y2 = rect

        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                graph[y][x] = 0
                
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    queue = deque([(characterX, characterY)])
    graph[characterY][characterX] = 2
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while queue:
        x,y = queue.popleft()
        
        if x == itemX and y == itemY:
            return (graph[y][x] - 2) // 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < SIZE and 0 <= ny < SIZE and graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))
                
    return answer
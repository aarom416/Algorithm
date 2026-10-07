from math import gcd

def solution(signals):
    
    limit = 1
    for s in signals:
        p = sum(s)
        limit = limit * p // gcd(limit, p)
    limit += 1
    
    graph = [[0] * limit for _ in range(len(signals))]
    
    for i in range(len(signals)):
        for j in range(signals[i][0]+1, limit, sum(signals[i])):
            for k in range(signals[i][1]):
                if j+k < limit:
                    graph[i][j+k] = 1
        
    for i in range(limit):
        count = 0
        for j in range(len(graph)):
            if graph[j][i] == 1:
                count += 1
            else:
                break
        if count == len(graph):
            return i
                    
    return -1

# 다른 풀이 - 현재 위치를 %로 표현해 g, y 의 범위 내 있는지 확인 (원래 풀이보다 메모리, 선능 측면에서 더 좋음)
from math import gcd

def solution(signals):
    
    limit = 1
    
    for g,y,r in signals:
        total = g+y+r
        limit = limit*total // gcd(limit, total)
        
    for i in range(1, limit+1):
        is_all_yellow = True
        
        for g,y,r in signals:
            total = g+y+r
            position = (i-1) % total
            
            if not (g <= position < g+y):
                is_all_yellow = False
        
        if is_all_yellow:
            return i
    return -1
    
    
            
        

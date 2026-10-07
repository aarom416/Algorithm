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
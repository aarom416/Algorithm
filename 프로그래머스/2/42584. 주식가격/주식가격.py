from collections import deque

def solution(prices):
    
    queue = deque(prices)
    answer = []
    
    while queue:
        current = queue.popleft()
        
        count = 0
        for q in queue:
            count +=1
            if current > q:
                break
                
                
        answer.append(count)
    return answer
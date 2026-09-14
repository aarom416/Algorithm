from collections import deque
def solution(priorities, location):
    
    queue = deque((i,p) for i,p in enumerate(priorities))

    result = []
    while queue:
        current = queue.popleft()
        for q in queue:
            if q[1] > current[1]:
                queue.append(current)
                break
        else:
            result.append(current)
        
    for i, (n,m) in enumerate(result):
        if location == n:
            return i+1
def solution(n):
    
    count = 0
    
    for _ in range(1, n+1):
        count +=1
        
        while count%3 == 0 or '3' in str(count):
            count+=1
        
    return count
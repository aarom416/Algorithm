def solution(citations):
    citations.sort(reverse=True)
    
    for i, c in enumerate(citations):
        if c < i+1:
            return i
        
    return len(citations)
    
        
    
            
        
    
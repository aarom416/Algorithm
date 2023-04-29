def solution(citations):
    citations.sort()
    max_value=citations[-1]
    answer=0
    if citations[0]>=len(citations):
        answer=len(citations)
        return answer
    for i in range(max_value+1):
        first=0
        second=0
        for j in citations:
            if j>=i:
                first+=1
            if j<=i:
                second+=1
        if first>=i and second>=0:
            answer=i
        else:
            return answer
    return answer
                
        
        
    
            
        
    
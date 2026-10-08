def solution(emergency):
    answer = []
    
    dic = {}
    
    sorted_emergency = sorted(emergency, reverse=True)
    
    for rank,e in enumerate(sorted_emergency):
        if e not in dic:
            dic[e] = rank+1
            
    for e in emergency:
        answer.append(dic[e])
    return answer
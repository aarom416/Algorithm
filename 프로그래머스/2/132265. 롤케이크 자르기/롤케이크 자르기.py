def solution(topping):
    answer = 0
    
    brother = {}
    
    for t in topping:
        if t in brother:
            brother[t] += 1
        else:
            brother[t] = 1
    
    chulsoo = {}
    
    for t in topping:
        if t in chulsoo:
            chulsoo[t] += 1
        else:
            chulsoo[t] = 1
            
        brother[t] -= 1
        if brother[t] == 0:
            del brother[t]
            
        if len(brother) == len(chulsoo):
            answer+=1
    return answer
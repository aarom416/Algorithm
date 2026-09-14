def solution(Progresses, Speeds):

    x = []
    for p,s in zip(Progresses, Speeds):
        
        if (100-p)%s == 0:
            x.append((100-p)//s)
        else:
            x.append((100-p)//s+1)
            
    temp = []      
    temp.append(x[0])
    
    answer = []
    
    for i in range(1, len(x)):
        
        if max(temp) < x[i]:
            answer.append(len(temp))
            while temp:
                temp.pop()
            temp.append(x[i])
        else:
            temp.append(x[i])
    
    answer.append(len(temp))
    
    return answer
    
    
    
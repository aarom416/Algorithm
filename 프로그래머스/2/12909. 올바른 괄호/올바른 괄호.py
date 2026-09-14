def solution(s):
    
    temp = []
    for i in s:
        if i == "(":
            temp.append(i)
        else:
            
            if len(temp) == 0 and i == ")":
                return False
            
            if len(temp) > 0 and temp[-1] == ")":
                return False
            
            if temp[-1] == "(":
                temp.pop()
                
            
    return len(temp) == 0
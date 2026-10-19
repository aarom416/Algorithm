def solution(s):    
    return Jaden_Case(s)
        
    
def Jaden_Case(s):
    return ' '.join([string.capitalize() for string in s.split(' ')])



## 다른 풀이 - 슬라이싱
def solution(s):    
    return ' '.join([string[0].upper() + string[1:].lower() for string in s.split(' ')])

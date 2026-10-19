def solution(s):    
    return Jaden_Case(s)
        
    
def Jaden_Case(s):
    return ' '.join([string.capitalize() for string in s.split(' ')])
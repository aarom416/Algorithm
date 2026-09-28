def solution(n, lost, reserve):
    answer = 0
    
    students = [1] * (n+2)
    
    for r in reserve:
        students[r] += 1
        
    for l in lost:
        students[l] -= 1
        
    for l in sorted(lost):
        if students[l] == 0:
            if students[l-1]>1:
                students[l-1] -= 1
                students[l] += 1
            elif students[l+1]>1:
                students[l+1] -= 1
                students[l] += 1
    
    return sum( 1 for s in students[1:n+1] if s > 0)

# 다른 풀이 set, remove 이용

def solution(n, lost, reserve):
    
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    
    for i in _lost:
        if i-1 in _reserve:
            _reserve.remove(i-1)
        elif i+1 in _reserve:
            _reserve.remove(i+1)
        else:
            n-=1
        
    return n

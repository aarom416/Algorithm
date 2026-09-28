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
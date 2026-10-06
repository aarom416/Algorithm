def solution(a, b):
    answer = 0
    
    big, small = max(a,b), min(a,b)
    
    for i in range(small, big+1):
        answer += i
    return answer
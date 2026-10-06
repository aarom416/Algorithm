def solution(numbers, k):
    answer = 0
    
    for i in range(k):
        answer = numbers[(2*i)%len(numbers)]
        
    return answer
def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
            
    return answer
def solution(my_str, n):
    answer = []
    
    list_str = ''
    for i, st in enumerate(my_str):
        list_str += st
        if i%n == n-1:
            answer.append(list_str)
            list_str = ''
        
    if list_str:
        answer.append(list_str)
    return answer
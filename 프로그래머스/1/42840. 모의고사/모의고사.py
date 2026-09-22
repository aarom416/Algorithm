def solution(answers):
    answer = []
    
    first_pattern = [1,2,3,4,5] * 2000
    second_pattern = [2,1,2,3,2,4,2,5] * 1250
    third_pattern = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    answer_count = 0
    first_right = 0
    second_right = 0
    third_right = 0
    
    for i,a in enumerate(answers):
        if first_pattern[i] == a:
            first_right +=1
        if second_pattern[i] == a:
            second_right +=1
        if third_pattern[i] == a:
            third_right +=1
            
    max_right = max(first_right, second_right, third_right)
    
    answer.append(first_right)
    answer.append(second_right)
    answer.append(third_right)
    
    result = []
    for i,a in enumerate(answer):
        if max_right == a:
            result.append(i+1)
            
    return result
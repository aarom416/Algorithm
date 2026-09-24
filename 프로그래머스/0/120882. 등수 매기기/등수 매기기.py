def solution(score):
    answer = [len(score)+1] * len(score)
    total = []
    
    sum_list = [a+b for a,b in score]

    sorted_sum_list = sorted(sum_list)
    
    for i, sl in enumerate(sum_list):
        for ssl in sorted_sum_list:
            if sl >= ssl:
                answer[i] -=1
        
    return answer
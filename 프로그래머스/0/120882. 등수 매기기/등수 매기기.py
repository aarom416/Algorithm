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

# 다른 풀이 - 해시 이용
def solution(score):
    
    rank = sorted([sum(s) for s in score], reverse=True)
    rank_dict = {}
    
    for i,r in enumerate(rank):
        if r not in rank_dict:
            rank_dict[r] = i+1
        
        
    return [rank_dict[sum(s)] for s in score]

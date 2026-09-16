from collections import Counter

def solution(nums):
    dic = Counter(nums)
    
    can_pick = len(nums)/2
    
    pick = 0
            
    for k,v in dic.items():
        can_pick -= 1
        pick += 1
        if can_pick == 0:
            return pick
    
    return len(list(dic.keys()))
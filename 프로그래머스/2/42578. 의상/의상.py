def solution(clothes):
    
    dic = {}
    
    for clothe, kind in clothes:
        if kind in dic:
            dic[kind].append(clothe)
        else:
            dic[kind] = [clothe]
    
    total_match = 1
    for k, v in dic.items():
        total_match *= (len(v) + 1)
    
    return total_match - 1
def solution(spell, dic):
    
    answer = [0] * len(dic)
    
    for i, d in enumerate(dic):
        for s in spell:
            if d.count(s) == 1:
                answer[i] += 1
    
    for a in answer:
        if a == len(spell):
            return 1
    return 2
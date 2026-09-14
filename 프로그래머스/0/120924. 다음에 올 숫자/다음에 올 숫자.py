def cal_db(common):
    return common[0] * common[2] == common[1]*common[1]
    
def solution(common):
    
    n = len(common)
    
    is_db = cal_db(common)
    
    if common[0] == 0 and common[1] == 0:
        return 0
    
    if is_db:
        r = common[1]//common[0]
        return common[0]*r**n
    else:
        d = common[1]-common[0]
        return common[0]+n*d
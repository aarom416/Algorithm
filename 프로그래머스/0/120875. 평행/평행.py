def solution(dots):
    
    incline1 = [calcuate_incline(dots[0], dots[1]), calcuate_incline(dots[0], dots[2]), calcuate_incline(dots[0], dots[3])]
    incline2 = [calcuate_incline(dots[1], dots[0]), calcuate_incline(dots[1], dots[2]), calcuate_incline(dots[1], dots[3])]
    incline3 = [calcuate_incline(dots[2], dots[0]), calcuate_incline(dots[2], dots[1]), calcuate_incline(dots[2], dots[3])]
    incline4 = [calcuate_incline(dots[3], dots[0]), calcuate_incline(dots[3], dots[1]), calcuate_incline(dots[3], dots[2])]
        
    temp1 = [];
    temp2 = [];
    
    for c1 in incline1:    
        for c2 in incline2:
            if c1 == c2:
                temp1.append(c1)
                
    for c3 in incline3:    
        for c4 in incline4:
            if c3 == c4:
                temp2.append(c3)
            
    for t1 in temp1:
        for t2 in temp2:
            if t1 == t2:
                return 1
                
    return 0

def calcuate_incline(dot1, dot2):
    return ((dot1[1]-dot2[1])/(dot1[0]-dot2[0]))
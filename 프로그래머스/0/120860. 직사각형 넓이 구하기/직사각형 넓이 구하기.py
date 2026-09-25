def solution(dots):
    answer = 0
    
    dots = sorted(dots, key=lambda x:(x[0],x[1]))
    
    y = dots[1][1] - dots[0][1] 
    x = dots[2][0] - dots[0][0]
    
    return x * y
def solution(bin1, bin2):
    b1,b2 = map(int, [bin1, bin2])
    
    b = list(str(b1 + b2))
    
    upper = 0
    for i in range(len(b)-1, -1, -1):
        str_b = int(b[i])
        
        if i == 0 and str_b > 1:
            upper = 1
            b[i] = str(int(b[i])-2)
            
        elif str_b > 1:
            b[i] = str(int(b[i])-2)
            b[i-1] = str(int(b[i-1]) + 1)
        
            
    if upper > 0:
        return str(upper) + ''.join(b)
    else:
        return ''.join(b)
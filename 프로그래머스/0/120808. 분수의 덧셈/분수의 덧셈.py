def solution(numer1, denom1, numer2, denom2):

    x = denom1 * denom2
    y = numer1 * denom2 + numer2 * denom1
    
    a = min(x,y)
    
    for i in range(a, 1, -1):
        if x%i == 0 and y%i == 0:
            x = x//i
            y = y//i
        
    return [y, x]

def solution(a, b):
    answer = 0
    
    m = min(a,b)
    
    for i in range(m, 0, -1):
        if a%i == 0 and b%i == 0:
            a = a//i
            b = b//i
    
    number = [2,5]
    
    if b == 1:
        return 1
    
    for n in number:
        while True:
            if b == 1:
                return 1
            if b%n == 0:
                b = b//n
                continue
            break
    
    return 2
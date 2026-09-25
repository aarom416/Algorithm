def solution(chicken):
    total_service = 0
    
    while chicken >= 10:
        service = chicken // 10
        rest = chicken % 10 + service
        total_service += service
        chicken = rest 
    
    return total_service
def solution(lines):
    count = [0] * 201
    
    for start, end in lines:
        for i in range(start, end):
            count[i] += 1
            
    return sum(1 for x in count if x >= 2)
    
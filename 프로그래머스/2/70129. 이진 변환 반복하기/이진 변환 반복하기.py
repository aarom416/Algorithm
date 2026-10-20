def solution(s):
    answer = []
    
    clean_s = s.replace('0', "")
    
    count = 0 
    remove_zero = 0
    
    while len(s) > 1:
        remove_zero += s.count('0')
        clean_s = s.replace('0', '')
        count += 1
        s = bin(len(clean_s))[2:]
    return [count, remove_zero]
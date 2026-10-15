def solution(s):
    
    numbers = list(map(int, s.split(' ')))
    
    return str(min(numbers)) + ' ' + str(max(numbers))
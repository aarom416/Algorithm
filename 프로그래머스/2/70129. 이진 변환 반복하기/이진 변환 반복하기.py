def solution(s):
    count = 0 
    remove_zero = 0
    
    while len(s) > 1:
        remove_zero += s.count('0')
        clean_s = s.replace('0', '')
        count += 1
        s = bin(len(clean_s))[2:]
    return [count, remove_zero]

# 다른 풀이 - bin() 함수 사용 X -> 이진변환함수 직접 구현
def solution(s):
    count = 0 
    remove_zero = 0
    
    while len(s) > 1:
        remove_zero += s.count('0')
        clean_s = s.replace('0', '')
        count += 1
        s = makeBin(len(clean_s))
    return [count, remove_zero]


def makeBin(a):
    
    answer = ''
    
    while a > 0:
        answer = str(a % 2) + answer
        a //= 2
    return answer
        

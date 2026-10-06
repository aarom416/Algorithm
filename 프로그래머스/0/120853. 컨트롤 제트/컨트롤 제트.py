def solution(s):
    answer = 0
    
    string = s.split(' ')
    
    for i,num in enumerate(string):
        if num == 'Z':
            answer -= int(string[i-1])
        else:
            answer += int(num)
    return answer
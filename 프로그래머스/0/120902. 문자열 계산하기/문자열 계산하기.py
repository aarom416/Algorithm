def solution(my_string):
    answer = 0
    
    string_list = my_string.split(' ')
    
    for i,s in enumerate(string_list):
        if s == '+':
            string_list[i+1] = str(int(string_list[i-1]) + int(string_list[i+1]))
        elif s == '-':
            string_list[i+1] = str(int(string_list[i-1]) - int(string_list[i+1]))
        else:
            continue
            
    return int(string_list[-1])

# 다른 풀이 - "-" 를 "+ -" 를 이용해서 "3 + 4 + -3" 형식
def solution(my_string):
    return sum(int(s) for s in my_string.replace(' - ', ' + -').split(' + '))

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
def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        temp = array[i-1:j]
        temp.sort()
        if len(temp) == 0:
            answer.append(array[k-1])
        else:
            answer.append(temp[k-1])
    return answer
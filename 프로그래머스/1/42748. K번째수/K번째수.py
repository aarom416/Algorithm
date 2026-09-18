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

## 다른 사람 풀이 - map(함수, 리터럴) 을 이용 함수 -> 람다식
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

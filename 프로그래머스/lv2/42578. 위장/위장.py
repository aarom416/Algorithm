def solution(clothes):
    answer = 1
    dic={}
    for i in range(len(clothes)): #종류별로 몇 개 있는지 구분
        if clothes[i][1] not in dic:
            dic[clothes[i][1]]=1
        else:
            dic[clothes[i][1]]+=1
    for value in dic.values(): #경우의 수 계산
        answer=answer*(value+1) #+1 는 해당 의상을 사용하지 않는 경우
    return answer-1 #모든 의상을 사용하지 않는 경우가 있으므로 -1 함

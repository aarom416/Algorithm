def solution(clothes):
    answer = 1
    total=1
    dic={}
    stack=[]
    dic[clothes[0][1]]=1
    for i in range(1,len(clothes)):
        if clothes[i][1] not in dic:
            dic[clothes[i][1]]=1
        else:
            dic[clothes[i][1]]+=1
    for value in dic.values():
        answer=answer*(value+1)
    return answer-1
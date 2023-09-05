from itertools import permutations
def valid(user,ban):
    if len(user)!=len(ban):
        return False
    else:
        for i,j in zip(user,ban): #zip 을 사용하여 각 문자를 비교
            if j=='*':
                continue
            elif i!=j:
                return False
        return True
    
def solution(user_id, banned_id):
    answer_list=[]
    arr=permutations(user_id,len(banned_id)) #순열 사용하여 순서를 포함하여 모든 조합을 리스트 형태로 나타냄
    for i in arr:
        count=0
        for a,b in zip(i,banned_id):
            if valid(a,b): #각 문자열의 문자들을 비교하여 유효한지 확인
                count+=1
        if count==len(banned_id) and set(i) not in answer_list: #'*'를 고려해 문자열이 동일하고 똑같은 조합 리스트가 존재하지 않은지 확인
            answer_list.append(set(i))
        
    return len(answer_list)
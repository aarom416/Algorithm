def solution(phone_book):
    answer = True
    dic={}
    flag=False
    for i in phone_book:
        dic[i]=len(i)
    for i in phone_book:
        string=""
        for j in i:
            string+=j
            if string in dic and string!=i:
                answer=False
                flag=True
                break
        if flag:
            break
    return answer
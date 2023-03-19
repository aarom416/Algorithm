def solution(phone_book):
    answer = True
    dic={}
    flag=False
    for i in phone_book:
        dic[i]=len(i)
    #하나의 번호에 대해 다른 번호를 비교하는게 아니라(=최대 O(n^2)) 번호의 접두어가 dic에 존재하는지로 시간복잡도 줄임(=최대 O(n*20))
    for i in phone_book: 
        string="" #문자 하나씩 받아 접두어를 구성해 dic에 존재하는지 확인할 임의의 문자열 선언
        for j in i:
            string+=j #하나씩 받기
            if string in dic and string!=i: #하나씩 받은 접두어가 dic에 존재하고 현재 문자열이 아니면
                answer=False
                flag=True
                break
        if flag:
            break
    return answer

def solution(name):
    answer = 0
    dic={}
    #A~N 까지 dic에 최소 움직임 저장 
    for i in range(14):
        dic[chr(65+i)]=i
    #M~Z 까지 dic에 최소 움직임 저장
    for i in range(12):
        dic[chr(90-i)]=i+1
    
    # A B C D E F G H I J K  L  M  N  O  P  Q  R S T U V W X Y Z
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 12 11 10 9 8 7 6 5 4 3 2 1 이렇게 저장
        
    min_move=len(name)-1 #초기 최단 길이
    for i in range(len(name)):
        answer+=dic[name[i]] # 위아래 움직이는 횟수 더함
        check=i+1 #현재 알파벳에서 다음 알파벳을 가리키는 check 변수
        while check<len(name) and name[check]=="A": #다음 알파벳이 A이면 연속되는지 확인하여 연속되는 마지막 A의 위치에 check가 가리키게 함
            check+=1
        min_move=min(min_move,i*2+len(name)-check,i+2*(len(name)-check)) 
        #i, check를 기준으로 (초기 최단 길이, i의 왼쪽 알파벳에 커서 움직인 횟수*2 + check의 오른쪽 알파벳에 커서 움직인 횟수, i의 왼쪽 알파벳에 커서 움직인 횟수 + check의 오른쪽 알파벳에 커서 움직인 횟수*2 ) 중 최솟값으로 계속 갱신하여 최소 이동거리 구함
        #i의 왼쪽 알파벳에 커서 움직인 횟수*2 + check의 오른쪽 알파벳에 커서 움직인 횟수, i의 왼쪽 알파벳에 커서 움직인 횟수 + check의 오른쪽 알파벳에 커서 움직인 횟수*2 --> 이렇게 두개로 나눈 이유는 ex) JENNAAAJE 이 경우 연속되는 3개의 A를 기준으로 왼쪽에 있는 JENN 을 두번 도는 것보다 오른쪽에 있는 JE를 두번 도는 것이 더 최소임
        # ex) JEAAAJENN 이 경우는 왼쪽에 있는 JE를 두번 도는 것이 더 최소이기 때문에 이러한 두 상황을 고려하여 min함수로 계속 비교하며 최소값을 갱신할 수 있도록 함
    answer+=min_move 
    return answer
            
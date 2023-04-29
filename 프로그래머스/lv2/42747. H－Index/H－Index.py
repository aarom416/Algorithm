def solution(citations):
    citations.sort() 
    max_value=citations[-1] #최대값 저장
    answer=0
    if citations[0]>=len(citations): #제일 작은 값이 전체 논문 횟수 보다 큰 경우 ex) [10,10,10]
        answer=len(citations) # 논문 횟수를 리턴
        return answer
    for i in range(max_value+1): 
        first=0 # 첫번째 조건을 만족하는 횟수 (h번 이상 인용된 논문이 h편 이상인 경우)
        second=0 # 두번째 조건을 만족하는 횟수 (나머지 논문이 h번 이하 인용된 경우)
        for j in citations: #조건 카운트
            if j>=i:
                first+=1
            if j<=i:
                second+=1
        if first>=i and second>=0: #h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 0보다 크면 됨
            answer=i #for 문 돌면서 알아서 최대값으로 설정됨
        else:
            return answer # 위 조건 만족하지 못하면 바로 리턴하여 시간 절약
    return answer # 한번 더 리턴한 이유는 [0,0,0,0,0,0] 처럼 위 조건을 계속 만족하여 else 문의 리턴이 진행되지 않는 경우를 고려하여 리턴 한번 더 함
                
        
        
    
            
        
    

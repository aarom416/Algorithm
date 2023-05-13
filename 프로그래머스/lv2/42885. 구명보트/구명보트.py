def solution(people, limit):
    answer = 0
    people.sort() #제일 무거운 사람과 제일 가벼운 사람을 묶어서 보트 보내는 게 최적이므로 오름차순으로 몸무게 정렬
    #시간 복잡도를 위해 투 포인터 사용
    left=0 
    right=len(people)-1
    while left<right:
        if people[left]+people[right]<=limit: #보트 들어갈 사람 찾았으면 
            answer+=1 #보트 개수 추가
            left+=1 #다음 가벼운 사람 선택
            right-=1 #다음 무거운 사람 선택
        else: #보트 들어갈 사람 못 찾았으면
            right-=1 #그 다음 무거운 사람 선택
    #전체 사람 수에서 보트 개수 뺀 이유는 처음에 제일 가벼운 사람을 기준으로 제일 무거운 사람 순으로 보기 떄문에 [50,70,80,90,100], 100 인경우 제일 가벼운 50,70 도 못태움 따라서 이땐 각각 보트를 한명 씩 타야 하므로 전체 사람수-보트를 만든 개수(두 사람을 보트 하나로 봄)를 해야함
    return len(people)-answer 

t = int(input())

for i in range(t):
    k,n = [int(input()) for _ in range(2)]
    floor = list(range(1,n+1))
    next_floor = [0]*n #다음 층 호수만큼 할당
    if k==0:
        print(n)
    else:
        for _ in range(k): #층 수만큼 반복
            for u in range(n): #호수만큼 반복
                next_floor[u] = sum(floor[:u+1]) 
                # 현재 층에 각 호수만큼의 합을 다음 층에 호수에 할당
            floor.clear() # 현재 층 삭제
            floor.extend(next_floor) 
            #next_floor=floor 이거 하면 floor.clear() 했기 떄문에 floor 는 null이므로 할당안됨
            #따라서 extend 로 null 인 floor 에 추가
    print(floor[len(floor)-1]) #마지막 호수 값 출력
    
    # 다른 풀이
    t = int(input())

for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력

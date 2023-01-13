n = int(input())

cnt = 0
while n>=0:
    if n%5==0: #5의 배수이면
        cnt+=(n//5) #개수 카운트
        print(cnt)
        break
    n-=3 #5의 배수 아니면 3씩 줄여가면서 카운트
    cnt+=1
    if n<0:
        print("-1")
        break
        
 # 다른 풀이
 
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)

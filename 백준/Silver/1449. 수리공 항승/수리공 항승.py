import sys
input=sys.stdin.readline
n,l=map(int,input().split())
location=list(map(int,input().split()))
location.sort()
max_location=location[-1] #최대값 저장
check=[True]*(max_location+l+1) #테이프 붙힌 곳을 표시할 check 리스트 최대값+테이프길이+1
cnt=0
flag=False #테이프를 새로 붙혔을때를 표시할 flag
for i in location: #물이 새고 있는 위치는 False 로 표시
    check[i]=False
for i in location:
    # 파이프 길이가 3이고 [1,2,3,4,5,6]인 경우 i가 1일때 1,2,3은 True
    # i가 2일때 2,3,4 중 2,3은 True, 4는 False 이므로 카운트 더하게 되므로 이렇게 계산하면 결과가 4가 나옴
    # [1,2,3],[4,5,6] 이렇게 결과값인 2가 나올 수 있게 하기 위해 테이프 붙인 부분이면 continue 해줌
    if check[i]: 
        continue
    for j in range(i,i+l): #위치부터 테이프 길이만큼 
        if not check[j]: #테이프 붙이지 않은거면
            check[j]=True #테이프 붙인거 표시
            flag=True #새로운 테이프 붙인 flag값 True
    if flag:
        cnt+=1 #새로 테이프 붙였으므로 cnt+=1
        flag=False
print(cnt)        

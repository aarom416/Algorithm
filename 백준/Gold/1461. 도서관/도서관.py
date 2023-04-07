import sys
input=sys.stdin.readline
n,m=map(int,input().split())
book=list(map(int,input().split()))
ans=0
check=[]
plus=[]
minus=[]
for i in book: #양수, 음수 분리
    if i>0:
        plus.append(i)
    else:
        minus.append(abs(i))
minus.sort(reverse=True) #양수, 음수 내림차순 정렬
plus.sort(reverse=True)
for i in range(len(minus)):  
    if i%m==0: #m으로 나눠지면 제일 큰 값을 갖는 수이므로 저장
        check.append(minus[i])
for i in range(len(plus)):
    if i%m==0:
        check.append(plus[i])
check.sort() #오름차순 정렬
ans=sum(check[:len(check)-1])*2+check[-1] #제일 큰 수를 제외하고 갔다오는 것까지 해서 *2해주고 마지막 제일 큰 수는 올 필요는 없으므로 가는 경우만 +해줌
print(ans)


    
    
        

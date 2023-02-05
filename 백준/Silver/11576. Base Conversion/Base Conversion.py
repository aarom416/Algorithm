a,b = map(int,input().split())
m=int(input())
num_list=list(map(int,input().split()))
sum=0
for i in range(len(num_list)):
    sum+=num_list[i]*a**(len(num_list)-1-i) #a진법 숫자를 10진법으로 변환
remainder=[]
while sum>=b: #10진법 숫자를 b진법으로 변환
    remainder.append(sum%b) #나머지 부분만 리스트 저장
    sum=sum//b
print(sum,*remainder[::-1]) #나머지 부분만 거꾸로 출력




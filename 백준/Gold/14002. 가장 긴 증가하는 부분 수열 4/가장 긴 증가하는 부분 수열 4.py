n = int(input())
num_list = list(map(int,input().split()))
dp=[1]*(n+1)
for i in range(1,n):
    for j in range(i):
        if num_list[j]<num_list[i]:
            dp[i+1]=max(dp[i+1],dp[j+1]+1) 
print(max(dp))
m=max(dp) #최대값 저장
stack=[] #최대값을 가지는 숫자부터 순서대로 삽입
for i in range(n,0,-1):
    if dp[i]==m:
        stack.append(num_list[i-1])
        m-=1
stack.reverse() #최대값부터 저장되어있으므로 거꾸로 만듬
print(*stack) #unpacking
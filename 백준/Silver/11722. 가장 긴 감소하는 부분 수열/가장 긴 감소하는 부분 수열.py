n = int(input())
num_list=list(map(int,input().split()))
dp=[1]*(n+1)
num_list.insert(0,0) #인덱스를 맞추기 위해 삽입
for i in range(2,n+1):
    for j in range(1,i):
        if num_list[i]<num_list[j]:
            dp[i]=max(dp[i],dp[j]+1) 
print(max(dp))
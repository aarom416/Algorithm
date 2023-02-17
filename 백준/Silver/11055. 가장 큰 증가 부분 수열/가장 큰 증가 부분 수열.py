n = int(input())
num_list=list(map(int,input().split()))
dp=[0]*(n+1)
num_list.insert(0,0) #인덱스를 맞추기 위해 삽입
dp[1]=num_list[1]
for i in range(2,n+1):
    for j in range(1,i):
        if num_list[i]>num_list[j]:
            dp[i]=max(dp[i],num_list[i]+dp[j]) #현재 num값+조건을 만족하는 dp값의 합과 현재 dp값 중 최대값으로 갱신
        else:
            dp[i]=max(dp[i],num_list[i])
print(max(dp))

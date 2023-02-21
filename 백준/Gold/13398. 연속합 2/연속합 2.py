n = int(input())
num_list=list(map(int,input().split()))
num_list.insert(0,0)
dp=[[-1001]*(n+1) for _ in range(2)]
dp[0][1]=-1001 #dp[0][]은 숫자를 제거한 경우
dp[1][1]=num_list[1] #dp[1][]은 숫자를 제거하지 않은 경우
for i in range(2,n+1):
    dp[0][i]=max(dp[0][i-1]+num_list[i],dp[1][i-1]) #그 전에 숫자를 제거한 dp+현재숫자 or 그 전까지 숫자를 제거하지 않은 dp(현재 숫자 제거) 중 최대값 
    dp[1][i]=max(dp[1][i-1]+num_list[i],num_list[i]) #그 전 숫자를 제거하지 않은 dp+현재 숫자 or 현재 숫자 중 최대값
print(max(max(dp[0]),max(dp[1])))
import sys
n = int(sys.stdin.readline().rstrip())
dp=[]
for i in range(n):
    dp.append(list(map(int,sys.stdin.readline().split())))
for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+dp[i][0] #현재 빨간집일때 최소값 (초록,파랑집 중 최소 + 빨간집 비용)
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+dp[i][1] #현재 초록집일때 최소값 (빨강,파랑 중 최소 + 초록집 비용)
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+dp[i][2] #현재 파란집일때 최소값 (빨강,초록 중 최소 + 파란집 비용)
print(min(dp[n-1]))
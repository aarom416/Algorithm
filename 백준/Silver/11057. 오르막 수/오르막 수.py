n = int(input())
dp=[[0]*10 for _ in range(n+1)]
dp[1]=[1,1,1,1,1,1,1,1,1,1]
for i in range(2,n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j]=(dp[i][j]+dp[i-1][k])%10007 #j=5면 k=1,2,3,4,5번째의 dp값 더해주면 됨
print(sum(dp[n])%10007)
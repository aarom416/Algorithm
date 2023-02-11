n = int(input())
dp=[[0]*10 for _ in range(n+1)]
dp[1]=[0,1,1,1,1,1,1,1,1,1]
if n==1:
    print(9)
    exit()
for i in range(1,n):
    for j in range(10):
        if j==0:
            dp[i+1][j]=dp[i][1]
        elif j==9:
            dp[i+1][j]=dp[i][8]
        else:
            dp[i+1][j]=dp[i][j-1]+dp[i][j+1]
print(sum(dp[n])%1000000000)
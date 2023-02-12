n = int(input())
if n==1 or n==2:
    print(1)
else:
    dp=[[0]*2 for _ in range(n+1)]
    dp[3][0]=1
    dp[3][1]=1
    for i in range(4,n+1):
        dp[i][0]=dp[i-1][0]+dp[i-1][1]
        dp[i][1]=dp[i-1][0]
    print(sum(dp[n]))

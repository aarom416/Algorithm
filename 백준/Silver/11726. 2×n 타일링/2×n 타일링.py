n = int(input())
dp=[0]*(n+1)
if n<=2:
    print(n)
else:
    dp[1],dp[2]=1,2
    for i in range(3,n+1):
        dp[i]=dp[i-2]+dp[i-1] #0,1,2,3,5,8 ... 순으로 증가 n-2번,n-1번의 합과 같음
    print(dp[-1]%10007)
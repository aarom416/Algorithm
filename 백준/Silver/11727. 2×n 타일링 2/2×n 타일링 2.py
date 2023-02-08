n = int(input())
if n==1:
    print(1)
elif n==2:
    print(3)
else:
    dp=[0]*(n+1)
    dp[1],dp[2]=1,3
    for i in range(3,n+1):
        dp[i]=2*dp[i-2]+dp[i-1] #0,1,2,3,5,8 ... 순으로 증가 n-2번의 2배와,n-1번의 합과 같음
    print(dp[-1]%10007)
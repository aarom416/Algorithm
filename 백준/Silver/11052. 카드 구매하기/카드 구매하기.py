n = int(input())
num_list = list(map(int, input().split()))
dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=num_list[i-1]
    j=i-1
    while True:
        if j==0:
            break
        dp[i]=max(dp[i],(i//j)*dp[j]+dp[i%j])
        j-=1
print(dp[n])



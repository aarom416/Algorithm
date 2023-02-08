t = int(input())
num_list = [int(input()) for _ in range(t)]
for i in num_list:
    if i==1:
        print(1)
    elif i==2:
        print(2)
    elif i==3:
        print(4)
    else:
        dp=[0]*(i+1)
        dp[1],dp[2],dp[3]=1,2,4
        for j in range(4,i+1):
            dp[j]=dp[j-3]+dp[j-2]+dp[j-1] #4번째 이후로 j-1,j-2,j-3 번째 합과 같음
        print(dp[j])


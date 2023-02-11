n = int(input())
dp=[[0]*10 for _ in range(n+1)]
dp[1]=[0,1,1,1,1,1,1,1,1,1] #n=1번째 부분 먼저 세팅
if n==1:
    print(9)
    exit()
for i in range(1,n):
    for j in range(10):
        if j==0: #0은 1에서 받을 수 밖에 없음(0에서 시작할 수 없으므로)
            dp[i+1][j]=dp[i][1]
        elif j==9: #9는 8에서 받을 수 밖에 없음
            dp[i+1][j]=dp[i][8]
        else: #그 외에는 위아래 더한 것과 같음 
            dp[i+1][j]=dp[i][j-1]+dp[i][j+1]
print(sum(dp[n])%1000000000)

import sys
tc=int(sys.stdin.readline().rstrip())
for _ in  range(tc):
    n=int(sys.stdin.readline())
    card=[]
    for _ in range(2):
        card.append(list(map(int,sys.stdin.readline().split())))
    dp=[[0]*(n+1) for _ in range(3)]
    dp[0][1]=0
    dp[1][1]=card[0][0]
    dp[2][1]=card[1][0]
    for i in range(2,n+1):
        dp[0][i]=max(dp[2][i-1],dp[1][i-1],dp[0][i-1])
        dp[1][i]=max(dp[0][i-1],dp[2][i-1])+card[0][i-1]
        dp[2][i]=max(dp[0][i-1],dp[1][i-1])+card[1][i-1]
    print(max(dp[0][n],dp[1][n],dp[2][n]))

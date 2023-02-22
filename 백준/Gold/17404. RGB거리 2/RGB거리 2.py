import sys
input=sys.stdin.readline
n = int(input())
house_cost=[list(map(int,input().split())) for _ in range(n)]
dp=[[0,0,0] for _ in range(n)]
INF=1000*1000+1
house_cost.insert(0,[0,0,0]) #insert로 인덱스 맞춰줌
dp.insert(0,[0,0,0]) #인덱스 맞춤
result=INF
for k in range(3): #빨강,초록,파랑 각각 시작할때로 구분
    dp[1]=[INF,INF,INF]
    dp[1][k]=house_cost[1][k]
    for i in range(2,n+1):
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])+house_cost[i][0]
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])+house_cost[i][1]
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])+house_cost[i][2]
    dp[n][k]=INF #마지막 집은 첫번째 집의 색과 달라야함-> INF로 선언
    result=min(result,min(dp[n]))
print(result)
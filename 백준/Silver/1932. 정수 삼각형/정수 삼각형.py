import sys
input=sys.stdin.readline
n = int(input())
dp=[list(map(int,input().split())) for _ in range(n)]
dp.insert(0,[0])
for i in range(1,n+1):
    for j in range(i):
        if j==0:
            dp[i][0]=dp[i-1][0]+dp[i][0]
        elif j==i-1:
            dp[i][j]=dp[i-1][j-1]+dp[i][j]
        else:
            dp[i][j]=max(dp[i-1][j-1]+dp[i][j],dp[i-1][j]+dp[i][j])
print(max(dp[n]))
# i=3이면 첫번째는 오른쪽 대각선 위의 dp 그대로 받고 현재dp값 더함 dp[3][0]=dp[2][0]+dp[3][0]
# 마지막은 왼쪽 대각선 위의 dp 그대로 받고 현재dp값 더함 dp[3][2]=dp[2][1]+dp[3][2]
# 중간에 있는 수는 왼쪽,오른쪽 대각선 위의 dp 값 중 최대값만 받고 현재dp 더하면 됨
# dp[3][1]=max(dp[2][1]+dp[3][1],dp[2][2]+dp[3][1])
# 이 식을 i,j로 표현하면 dp[i][0]=dp[i-1][0]+dp[i][0],dp[i][j]=dp[i-1][j-1]+dp[i][j],
# dp[i][j]=max(dp[i-1][j-1]+dp[i][j],dp[i-1][j]+dp[i][j])
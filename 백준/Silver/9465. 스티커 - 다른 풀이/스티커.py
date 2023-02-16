import sys
tc=int(sys.stdin.readline().rstrip())
for _ in  range(tc):
    n=int(sys.stdin.readline())
    card=[]
    for _ in range(2):
        card.append(list(map(int,sys.stdin.readline().split())))
    dp=[[0]*(n+1) for _ in range(3)] #dp[0][]은 모든 카드가 존재하지 않을때, dp[1][]은 위 카드만 존재할때, dp[2][]는 아래 카드만 존재할때로 구분
    dp[0][1]=0
    dp[1][1]=card[0][0]
    dp[2][1]=card[1][0]
    for i in range(2,n+1):
        dp[0][i]=max(dp[2][i-1],dp[1][i-1],dp[0][i-1]) #모든 카드 존재하지 않을때 그 전 dp의 최대값만 구하면 됨
        dp[1][i]=max(dp[0][i-1],dp[2][i-1])+card[0][i-1] #위 카드만 존재할때 그 전 아래카드가 존재했을때 dp와 그 전 카드가 존재하지 않을때 dp값 중 최대값과 현재 카드값을 더한 값으로 구함
        dp[2][i]=max(dp[0][i-1],dp[1][i-1])+card[1][i-1] #아래 카드만 존재할때 그 전 위카드가 존재했을때 dp와 그 전 카드가 존재하지 않을때 dp값 중 최대값과 현재 카드값을 더한 값으로 구함
    print(max(dp[0][n],dp[1][n],dp[2][n]))

#다른 풀이
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    n = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]
    if n > 1 :
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2,N) :
        dp[0][i] += max(dp[1][i-1],dp[1][i-2])
        dp[1][i] += max(dp[0][i-1],dp[0][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))
#지그재그로 가는 경우의 과정에서 한칸을 건너뛰는 경우와 
#계속 지그재그로 가는 경우를 비교하며 DP값을 저장한 후 최댓값을 구하는 걸로 코드를 구현

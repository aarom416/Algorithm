import sys

input = sys.stdin.readline

n,k = map(int,input().split())

moneys = [int(input().rstrip()) for _ in range(n)]
dp = [0]+[10001]*(k)
moneys.sort()
for money in moneys:
    for i in range(money,k+1):
      dp[i] = min(dp[i],dp[i-money]+1) #money만큼 전에 있는 dp 값에 money 만 더해주면 되므로 +1
if dp[k]==10001:
    print(-1)
else:
    print(dp[k])
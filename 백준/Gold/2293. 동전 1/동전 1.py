import sys

input = sys.stdin.readline

n,k = map(int,input().split())
coins = [int(input().rstrip()) for _ in range(n)]

dp = [1]+[0]*(k)

for coin in coins:
    for i in range(coin,k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]
               
print(dp[k])
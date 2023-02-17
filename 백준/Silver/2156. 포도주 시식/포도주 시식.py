import sys
input=sys.stdin.readline
n = int(input())
wine=[int(input()) for _ in range(n)]
wine.insert(0,0)
dp=[0]*(n+1)
if n>1:
    dp[1]=wine[1]
    dp[2]=wine[1]+wine[2]
    for i in range(3,n+1):
        dp[i]=max(wine[i]+dp[i-2],dp[i-1],dp[i-3]+wine[i-1]+wine[i])
    print(dp[n])
else:
    print(wine[1])
#i=1일때 dp[1]=wine1, i=2 dp[2]=wine1+wine2, i=3 dp[3]=max(wine1+wine2,wine1+wine3,wine2+wine3)
#dp[3]의 경우의 수에서 wine1 + wine2는 dp[2]와 같음
#dp[4]의 경우의 수를 보면 wine2 + wine3은 dp[3]이고, wine1 + wine2 + wine4에서 wine1 + wine2는 dp[2]
#그리고 wine1 + wine3 + wine4에서 wine1은 dp[1]
#dp[4]의 경우의 수 : dp[4 - 1], dp[4 - 3] + wine[4 - 1] + wine[4], dp[4 - 2] + wine[4]
#4를 i로 바꾸면 dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i] 


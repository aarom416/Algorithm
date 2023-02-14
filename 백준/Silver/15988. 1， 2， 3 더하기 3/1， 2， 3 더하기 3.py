import sys
tc = int(sys.stdin.readline().rstrip())
dp=[0]*1000001
dp[1],dp[2],dp[3]=1,2,4
MOD=1000000009
for i in range(4,1000001):
    #i=4이면 i=1일때 뒤에 3만 붙이고, i=2일때 뒤에 2만 붙이고, i=3일때 뒤에 1만 붙이면 됨
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%MOD
for _ in range(tc):
    n = int(sys.stdin.readline())
    print(dp[n])
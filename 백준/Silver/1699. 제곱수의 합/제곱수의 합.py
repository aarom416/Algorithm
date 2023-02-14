import sys
n = int(sys.stdin.readline())
dp = [k for k in  range(n+1)] #제곱수를 포함할때마다 개수가 +1되므로 초기값 k로 선언
for i in range(1,n+1):
    for j in range(1,i):
        if j*j>i: #제곱수 넘어가면 볼 필요 없음
            break
        if dp[i]>dp[i-j*j]+1:
            #i=5, j는 2까지만 루프돌고 i=1일때에서 2^2 만 더해주면 됌(즉 개수는 +1만 해주면 됌) 
            dp[i]=dp[i-j*j]+1
print(dp[n])

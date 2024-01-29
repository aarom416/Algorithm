import sys

input = sys.stdin.readline

code = [0]+list(input().rstrip())

if code[1]=='0': #처음이 0이면 만들 수 없음
    print(0)
    exit()

dp = [0]*(len(code))
dp[0]=1
dp[1]=1

for i in range(2,len(code)):
     #일의 자리수
    first = int(code[i])
    #십의 자리수까지 구해서 10이상 26이하인지 확인 -> 조건이 맞으면 십의자리와 일의 자리로 암호를 만들 수 있으므로 i-2번째 dp 를 더해주면 됨
    tenth = int(code[i-1])*10+int(code[i]) 
    if tenth>=10 and tenth<=26:
        dp[i] += dp[i-2]
    if first > 0:
        dp[i] += dp[i-1]

print(dp[len(code)-1]%1000000)
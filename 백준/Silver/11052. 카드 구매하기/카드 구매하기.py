n = int(input())
num_list = list(map(int, input().split())) #P(i) 값 num_list로 받음
dp=[0]*(n+1) #dp 테이블 초기화(n팩을 살때 최대 금액을 넣을 테이블)
for i in range(1,n+1):
    dp[i]=num_list[i-1] #dp테이블에 해당한는 P(i)값은 한칸 뒤에 있음
    #P(i)값을 그대로 저장하는 것은 현재 i를 i로 나눈 것을 미리 저장하는 것을 의미 ex)n=4면 4로 나눈 값(=P(4))을 미리 저장
    j=i-1
    while True: #ex)n=4, j=3,2,1 순서대로 몫과 나머지를 구해 현재 dp값과 비교
        if j==0:
            break
         #ex)n=4,j=2 이면 i//j:2 i%j:2 -> j번째 dp값을 갖는(j팩을 살때 최대 금액)값*2 와
         #나머지 2에 위치한 dp(2팩을 살때 최대금액)을 더한 값을 현재 dp와 최대인지 비교
        dp[i]=max(dp[i],(i//j)*dp[j]+dp[i%j])
        j-=1
print(dp[n])

#다른 풀이
n = int(input())
p = list(map(int, input().split()))
p.insert(0,0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], p[j] + dp[i-j])
print(dp[n])
3 5 15 16 을 예시로 들자.

#dp[1] 은 언제나 p[1] 과 동일할 것이므로 3
#dp[2] 는 dp[1] + p[1] 또는 p[2] 둘 중 큰 값일 것이므로 8
#dp[3] 은 dp[1] + p[2] , dp[2] + p[1] , p[3] 중 큰 값일 것이므로 15
#마지막으로 dp[4] 는 dp[1] + p[3] , dp[2] + p[2] , dp[3] + p[1] , p[4] 중 큰 값이므로 18

 



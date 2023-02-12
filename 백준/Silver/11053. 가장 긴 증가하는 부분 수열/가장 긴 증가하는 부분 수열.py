n = int(input())
num_list = list(map(int,input().split()))
dp=[1]*(n+1) #가장 긴 증가하는 부분 수열 개수를 나타내는 dp테이블
for i in range(1,n):
    for j in range(i):
        if num_list[j]<num_list[i]:
            #현재 자신의dp값과 if문을 만족하는 위치의 값+1 중에 최대값 선택해야 수열의 최대 개수 세짐
            dp[i+1]=max(dp[i+1],dp[j+1]+1) #dp는 0번부터 시작하므로 i+1,j+1로 순서맞춤
print(max(dp))
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
dp=[[0]*(k+1) for _ in range(n+1)]
weight_list=[]
value_list=[]
for _ in range(n):
    w,v=map(int,input().split())
    weight_list.append(w) #무게 리스트 선언
    value_list.append(v) #가치 리스트 선언
#각 물건에 따라 최적의 가치를 구해야함
for i in range(n+1): #각 물건을 추가하는 식으로 구하기 위해 i는 각 물건 번호
    for j in range(k+1): #각 무게에 따른 최대 가치를 구하기 위해 j는 각 무게
        if i==0 or j==0: 
            dp[i][j]=0
        elif j-weight_list[i-1]>=0: #각 무게에 따라 최대 버틸 수 있는 무게 보다 작거나 같으면
            # 현재 물건을 기준으로 현재 물건의 가치 + 전 물건에서 현재 물건의 무게를 뺀 부분의 최대가치와 현재 물건을 사용하지 않고 현재 무게를 만족하는 그 전 물건에서의 무게 중에서 최대 값 구함 
            # 물건은 한번 사용하면 다시 사용 못하므로 이렇게 설정
            dp[i][j]=max(value_list[i-1]+dp[i-1][j-weight_list[i-1]],dp[i-1][j])
        else: #최대 버틸 수 있는 무게보다 크면 현재 무게에 해당하는 전 물건의 최대 가치로 설정
            dp[i][j]=dp[i-1][j]
print(dp[n][k])

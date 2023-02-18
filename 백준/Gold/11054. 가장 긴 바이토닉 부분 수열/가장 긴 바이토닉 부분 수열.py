n = int(input())
num_list=list(map(int,input().split()))
reverse_num_list=num_list[::-1]
num_list.insert(0,0) #인덱스를 1부터 사용하기 위해 삽입
reverse_num_list.insert(0,0) #인덱스를 1부터 사용하기 위해 삽입
increase_dp=[1]*(n+1)
decrease_dp=[1]*(n+1)
result_dp=[0]*(n+1)
for i in range(2,n+1):
    for j in range(1,i):
        if num_list[i]>num_list[j]:
            increase_dp[i]=max(increase_dp[i],increase_dp[j]+1)
        if reverse_num_list[i]>reverse_num_list[j]:
            decrease_dp[i]=max(decrease_dp[i],decrease_dp[j]+1)
for i in range(1,n+1):
    result_dp[i]=increase_dp[i]+decrease_dp[n-(i-1)]-1
    #decrease_dp는 역순으로 값이 저장되어 있으므로 뒤부터 더함
    #이때 해당 인덱스 dp 값이 increase,decrease에서 두번 더해지므로 -1
print(max(result_dp))
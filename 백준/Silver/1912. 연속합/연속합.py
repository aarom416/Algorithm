import sys
n=int(sys.stdin.readline().rstrip())
num_list=list(map(int,sys.stdin.readline().split()))
for i in range(1,n): #i-1과 i번째의 합과 i번째 합과 비교하여 더 큰 것으로 리스트 초기화
    num_list[i]=max(num_list[i],num_list[i-1]+num_list[i])
print(max(num_list))
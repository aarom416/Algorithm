import sys

n = int(input())
number_list = list(map(int,input().split()))    
stack = [number_list[0]] 
dp = [1]*(n+1) #각 원소별로 최대 증가하는 수열을 저장하기 위한 dp

#이분 탐색 실행
def binary_search(target):
    start = 0
    end = len(stack)-1
    while start<=end:
        mid = (start+end)//2
        if stack[mid]<target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(1,n):
    if stack[-1] < number_list[i]:
        stack.append(number_list[i])
        dp[i+1] = len(stack) #개수만큼 dp 업데이트
    else:
        idx = binary_search(number_list[i]) #이분 탐색으로 위치시켜야할 해당 인덱스 값 추출
        stack[idx] = number_list[i] #해당 인덱스에 값 삽입
        dp[i+1]=idx+1 #위치시켜야할 인덱스 값 삽입하여 해당 값이 어디에 위치해 있는지 적음

result = []
m = max(dp)
for i in range(n,-1,-1): #dp의 최대값을 역추적하여 원소 값을 찾음
    if dp[i]==m:
        result.append(number_list[i-1])
        m-=1
result.reverse()

print(max(dp))
print(*result)

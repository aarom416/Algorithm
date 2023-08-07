import sys
input=sys.stdin.readline
first=input().rstrip()
second=input().rstrip()
dp=[0]*len(second) #리스트 하나만 사용하여 메모리 절약 및 속도 증가
for i in range(len(first)):
    count=0 #누적된 문자열 개수
    for j in range(len(second)):
        if count<dp[j]: #뮨자가 다르고 현재 누적 문자열 개수보다 현재 dp 값이 크다는 것은 현재 dp 값에 더 많이 문자열이 누적되어 있다는 의미
            count=dp[j] #따라서 현재 dp 값으로 현재 누적 문자열 개수 갱신
        elif first[i]==second[j]: #문자가 같으면 누적 문자열 개수+1
            dp[j]=count+1
#주의할 점은 XXXXF,XXXEX 와 같이 한 문자가 둘 다 반복되어 있는 경우 누적 값이 추가 되지 않으므로 
#누적 문자열 개수가 현재 dp 값보다 작은지 먼저 확인해야함
print(max(dp))
            
import sys

input = sys.stdin.readline

n = int(input())
lines = [list(map(int,input().split())) for _ in range(n)]
dp=[1]*(n+1)

lines.sort(key=lambda x : x[0]) #A 전봇대 기준으로 오름차순 정렬

#각 전깃줄에서 교차하지 않은 최대 전깃줄의 개수를 구하는 dp
for i in range(1,n): 
    for j in range(i):
        if lines[j][1] < lines[i][1]:
            dp[i+1] = max(dp[i+1],dp[j+1]+1) #dp 갱신
print(n-max(dp))
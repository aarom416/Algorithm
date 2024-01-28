import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
        
for _ in range(t):           
    n,k = map(int,input().split())
    buildings = list(map(int,input().split()))
    graph = [[] for _ in range(n+1)] #건물들의 이어진 경로를 담을 그래프
    inDegree = [0 for _ in range(n+1)] #진입차수
    dp = [0 for _ in range(n+1)] #최대 건설 시간을 담을 dp 
    
    for _ in range(k):
        a,b = map(int,input().split())
        graph[a].append(b)
        inDegree[b]+=1
                
    target = int(input().rstrip())
    
    q = deque()
    for i in range(1,n+1): #진입 횟수 0인 것부터 확인하기 위해 큐에 넣음
        if inDegree[i] == 0:
            q.append(i)
            dp[i]=buildings[i-1]

    while q:
        x = q.popleft()
        for i in graph[x]:
            inDegree[i]-=1 #진입 횟수 하나 줄임
            dp[i]=max(dp[i],dp[x]+buildings[i-1]) #현재 진입한 dp 값과, 진입하기 전에 dp 값 + 현재 진입한 건물의 건설시간 중 최대로 dp 갱신
            if inDegree[i]==0: #진입 횟수 0이 되면 큐에 추가
                q.append(i)
    
    print(dp[target])
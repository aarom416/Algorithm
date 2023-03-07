import sys
sys.setrecursionlimit(10**6) #파이썬은 재귀깊이가 1000으로 설정되있으므로 그 이상 재귀호출이 일어날 수 있게 설정해줌
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
cnt=0
def dfs(x):
    visited[x]=True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)    
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    if not visited[i]: #방문 안한 것들만 방문
        dfs(i)
        cnt+=1
print(cnt)
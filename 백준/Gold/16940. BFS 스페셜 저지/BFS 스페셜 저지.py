import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
level=[[] for _ in range(n+1)]
visited=[False]*(n+1)
def bfs():
    q=deque()
    q.append(1)                
    visited[1]=True
    idx=1
    while q:
        x=q.popleft()
        child=[]
        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                child.append(i)
        if sorted(ans[idx:idx+len(child)])==sorted(child):
            for j in ans[idx:idx+len(child)]:
                q.append(j)
            idx+=len(child)
        else:
            return 0
    return 1
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans=list(map(int,input().split()))
if ans[0]==1:
    print(bfs())
else:
    print(0)
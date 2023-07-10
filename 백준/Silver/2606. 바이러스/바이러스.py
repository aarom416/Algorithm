from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
k=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(k):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(x):
    count=0
    q=deque()
    q.append(x)
    while q:
        x=q.popleft()
        visited[x]=True
        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                count+=1
    return count
print(bfs(1))
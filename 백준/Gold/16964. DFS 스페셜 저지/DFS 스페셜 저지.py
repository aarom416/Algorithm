import sys
from collections import deque
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
def dfs():
    x=ans.popleft()
    if not ans:
        print(1)
        exit()
    visited[x]=True
    for _ in range(len(graph[x])):
        if ans[0] in graph[x] and not visited[ans[0]]:
            dfs()
    return False
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans=deque(map(int,input().split()))
if ans[0]==1:
    if not dfs():
        print(0)
else:
    print(0)

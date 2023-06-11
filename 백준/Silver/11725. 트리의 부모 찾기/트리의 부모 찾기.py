import sys
from collections import deque
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
parent_node=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x]=True
    for i in graph[x]:
        if not visited[i]:
            parent_node[i]=x #부모 노드 저장
            dfs(i)
dfs(1)
for i in range(2,len(parent_node)):
    print(parent_node[i])
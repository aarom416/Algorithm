import sys
from collections import deque
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
def dfs():
    x=ans.popleft() #제일 앞에 있는 숫자 뽑기 -> 현재 부모 노드
    if not ans: #리스트가 다 비면 올바른 순환이라는 의미
        print(1)
        exit()
    visited[x]=True
    for _ in range(len(graph[x])): #현재 부모 노드와 연결된 자식 노드 개수만큼 루프 돌면서 
        if ans[0] in graph[x] and not visited[ans[0]]: #자식노드가 맞는지 확인 
            dfs()
    return False #만약 자식노드가 아니라면 재귀 돌다가 False 리턴
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans=deque(map(int,input().split())) #맨 앞 값을 popleft 하여 사용하기 위해 deque 선언
if ans[0]==1:
    if not dfs():
        print(0)
else:
    print(0)

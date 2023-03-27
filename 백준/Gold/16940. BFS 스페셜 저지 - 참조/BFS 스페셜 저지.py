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
    idx=1 #자식노드의 첫 인덱스
    while q:
        x=q.popleft()
        child=[] #자식노드 리스트
        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                child.append(i) #현재 부모 노드에 대한 자식 노드 삽입
        #답(=ans)에서 자식노드만 slicing을 통해 정렬한 것과 현재 자식 노드를 정렬한 것이 같으면 
        if sorted(ans[idx:idx+len(child)])==sorted(child): 
            for j in ans[idx:idx+len(child)]: #다음 자식노드 확인을 위해 q에 삽입
                q.append(j)
            idx+=len(child) #idx 업데이트
        else:
            return 0 #같지 않으면 0 리턴
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

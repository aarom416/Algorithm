from collections import deque
n,m=map(int,input().split())
relations=[[] for _ in range(n)]
visited=[False]*n
#친구 관계 정리
for _ in range(m):
    a,b=map(int,input().split())
    relations[a].append(b)
    relations[b].append(a)
#dfs를 사용하여 깊이가 5가 되면 1출력 
def dfs(idx,depth):
    if depth==4:
        print(1)
        exit()
    for i in relations[idx]:
        if not visited[i]: #방문
            visited[i]=True 
            dfs(i,depth+1)
            visited[i]=False #모든 노드의 깊이를 확인하기 위해 dfs 끝나면 방문 False 처리
for i in range(n):
    visited[i]=True
    dfs(i,0)
    visited[i]=False #모든 노드의 깊이를 확인하기 위해 dfs 끝나면 방문 False 처리
print(0)
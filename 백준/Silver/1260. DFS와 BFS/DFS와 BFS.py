from collections import deque
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
dfs_visited=[False]*(n+1)
bfs_visited=[False]*(n+1)
dfs_stack=[]
bfs_stack=[]
def dfs(x):
    dfs_visited[x]=True
    dfs_stack.append(x)
    for i in graph[x]:
        if not dfs_visited[i]:
            dfs(i)
    return dfs_stack
def bfs(x):
    q=deque([x])
    bfs_visited[x]=True
    while q:
        v=q.popleft()
        bfs_stack.append(v)
        for i in graph[v]:
            if not bfs_visited[i]:
                bfs_visited[i]=True
                q.append(i)
    return bfs_stack
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort() #정점 번호가 작은 것부터 먼저 방문하기 위해 오름차순 정렬
    graph[b].sort() #정점 번호가 작은 것부터 먼저 방문하기 위해 오름차순 정렬
print(*dfs(v))
print(*bfs(v))
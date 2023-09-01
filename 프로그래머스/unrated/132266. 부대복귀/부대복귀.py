from collections import deque
def bfs(x,info,visited,sources):
    q=deque()
    q.append(x)
    visited[x]+=1
    while q:
        x=q.popleft()
        for i in info[x]:
            if visited[i]==-1:
                q.append(i)
                visited[i]=visited[x]+1
    return [visited[i] for i in sources]
def solution(n, roads, sources, destination):
    info=[[] for _ in range(n+1)]
    answer=[]
    for i,j in roads:
        info[i].append(j)
        info[j].append(i)

    visited=[-1]*(n+1)    
    return bfs(destination,info,visited,sources)
    

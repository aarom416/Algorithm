from collections import deque
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
stack=deque()
ans=-2
def bfs():
    q=deque()
    while stack:
        i,j=stack.popleft()
        q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            stack.append((i,j))
bfs()
for i in range(n):
    if 0 in graph[i]:
        print(-1)
        exit()
    ans=max(ans,max(graph[i]))
print(ans-1)

import sys
from collections import deque
input=sys.stdin.readline
m,n,k=map(int,input().split())
graph=[[0]*n for _ in range(m)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
area_list=[]
for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y2-y1):
        for j in range(x2-x1):    
            if not graph[y1+i][x1+j]:
                graph[y1+i][x1+j]=1
def bfs(a,b):
    graph[a][b]=1
    area=1
    q=deque()
    q.append((a,b))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            elif graph[nx][ny]==1:
                continue
            else:
                graph[nx][ny]=1
                q.append((nx,ny))
                area+=1
    area_list.append(area)
count=0    
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            bfs(i,j)
            count+=1
area_list.sort()
print(count)
print(" ".join(map(str,area_list)))

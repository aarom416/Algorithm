from collections import deque
import sys
input=sys.stdin.readline
t=int(input())
dx=[1,-1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    q=deque()
    q.append([x,y])    
    graph[x][y]=2
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                q.append([nx,ny])
                graph[nx][ny]=2
                
for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    cnt=0
    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1
    for i in range(n): #행, 열 구분 잘하기
        for j in range(m):
            if graph[i][j]==1:
                cnt+=1
                bfs(i,j)
    print(cnt)            
    
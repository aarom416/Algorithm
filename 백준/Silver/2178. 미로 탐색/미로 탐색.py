from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(map(int,input().rstrip())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1 #전 위치의 값에서 +1
                q.append((nx,ny))
    return graph[n-1][m-1] #마지막 위치의 값 리턴
print(bfs(0,0))

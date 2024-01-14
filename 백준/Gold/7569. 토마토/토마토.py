import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1] #3차원 배열 생성
result = 0
def bfs():
    q = deque()
    for k in range(h): #토마토 위치 모두 확인 후 처리
        for i in range(n):
            for j in range(m):
                if graph[k][i][j]==1:
                    q.append((k,i,j))
    while q:
        z,x,y= q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or nz<0 or nz>=h:
                continue
            if graph[nz][nx][ny]==0:
                graph[nz][nx][ny]=graph[z][x][y]+1
                q.append((nz,nx,ny))
    
bfs()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j]==0:
                print(-1)
                exit()
            result = max(result,max(graph[k][i]))
print(result-1) #모두 1인 경우(익은 토마토만 있는 경우) 알아서 0으로 처리 

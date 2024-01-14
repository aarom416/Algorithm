#나의 풀이 - 2차원으로 접근해 높이(n)만큼 위,아래만 추가로 bfs 진행하면 될 것 같았으나
# 3 3 2
# -1 -1 -1
# -1 -1 -1
# -1 0 -1
# -1 1 -1
# -1 -1 -1
# -1 -1 -1 
# 위처럼 상자위 위아래로 나뉘어져 있기 때문에 (1,3)에 위치한 익은 토마토가 (1,2)에 위치한 안익은 토마토에 영향을 주면 안되는데 내 코드는 하나의 graph 로 접근하기 때문에
# 안익은 토마토에 접근해 익은 토마토로 바뀜 -> 이 때문에 3차원 배열로 접근하여 다른 상자로 구분해놓은게 중요함

import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n*h)]
dx = [1,-1,0,0,n,-n] #밑 상자부터 순서대로 입력받음 -> 3차원 배열 쓰지 않고 높이만큼 더해주고 빼주어 위,아래 조건 성립
dy = [0,0,1,-1,0,0]
result = -2
def bfs():
    global result
    global flag
    q = deque()
    for i in range(n*h):
        for j in range(m):
            if graph[i][j]==1:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n*h or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
    

bfs()

for i in range(n*h):
    for j in range(m):
        if graph[i][j]==0:
            print(-1)
            exit()
        result = max(result,graph[i][j])
if result == 1: 
    print(0)
else:
    print(result-1)

# 다른 풀이 - 3차원 배열 접근
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

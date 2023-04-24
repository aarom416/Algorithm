#다익스트라 알고리즘과 같음
import sys
from collections import deque
input=sys.stdin.readline
m,n=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))
dist=[[-1]*m for _ in range(n)] #벽 부싯 횟수를 저장할 리스트
dist[0][0]=0
dx=[1,-1,0,0]
dy=[0,0,-1,1]
def bfs():
    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if dist[nx][ny]==-1: #방문하지 않고
                if graph[nx][ny]==0: #벽이 없으면
                    dist[nx][ny]=dist[x][y] #벽 부시는 횟수 그대로
                    q.appendleft((nx,ny)) #벽이 없는 부분을 우선순위 두고 먼저 확인할 수 있게 함
                else: #벽이 있으면
                    dist[nx][ny]=dist[x][y]+1 #벽 부신 횟수 +1 해줌
                    q.append((nx,ny)) 
bfs()
print(dist[n-1][m-1])

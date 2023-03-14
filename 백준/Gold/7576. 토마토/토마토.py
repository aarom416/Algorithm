from collections import deque
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
ans=-2
def bfs():
    while q: 
        x,y=q.popleft() #익은 토마토가 위치했던 곳부터 bfs 수행-> 각가 한번씩 상하좌우 +1 반복됨
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: #벽인 경우 continue
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1 #날짜 증가
                q.append((nx,ny))

for i in range(n): # 익은 토마토 위치 찾기
    for j in range(m):
        if graph[i][j]==1:
            q.append((i,j))
bfs() #토마토가 다 익는 날짜 세는 bfs 수행
for i in range(n):
    if 0 in graph[i]: #각 행마다 익지 않은 토마토가 존재하는지 확인
        print(-1) #있으면 -1 출력 후 종료
        exit()
    ans=max(ans,max(graph[i])) # 다 익었으면 각 행 중 최대값과 결과값과 비교하여 최대값 저장
print(ans-1) #1부터 시작했으므로 -1 후 출력

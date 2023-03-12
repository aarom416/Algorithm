from collections import deque
import sys
input=sys.stdin.readline
dx=[-1,-2,-2,-1,1,2,2,1]
dy=[2,1,-1,-2,-2,-1,1,2]
def bfs(s_x,s_y,e_x,e_y):
    q=deque()
    q.append((s_x,s_y))
    while q:
        x,y=q.popleft()
        if x==e_x and y==e_y:
            print(graph[x][y]-1) #맨 처음 위치값이 1부터 시작했으므로 -1 해줌
            return
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
k=int(input())
for i in range(k):
    n=int(input())
    graph=[[0]*n for _ in range(n)]
    start_x,start_y=map(int,input().split())
    end_x,end_y=map(int,input().split())
    graph[start_x][start_y]=1
    bfs(start_x,start_y,end_x,end_y)

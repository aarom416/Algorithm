from collections import deque
import sys
sys.setrecursionlimit(10**6) #파이썬은 재귀깊이가 1000으로 설정되있으므로 그 이상 재귀호출이 일어날 수 있게 설정해줌
input=sys.stdin.readline
def bfs(x,y):
    global cnt
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==0:
                continue
            if not visited[nx][ny] and graph[nx][ny]==1:
                visited[nx][ny]=True
                q.append((nx,ny))
                cnt+=1
    stack.append(cnt)
n=int(input())
graph=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
stack=[]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]==1:
            cnt=1
            bfs(i,j)
print(len(stack))
stack.sort()
for i in stack:
    print(i)
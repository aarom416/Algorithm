from collections import deque
import copy
import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
island=[[False]*n for _ in range(n)]
cnt=2
cnt_stack=[]
q=deque()
ans=[]
def bfs(temp,q,cnt):
    a=[]
    q=deque(q)
    while q: 
        x,y=q.popleft() 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: #벽인 경우 continue
                continue
            if temp[nx][ny]==cnt:
                continue
            if temp[nx][ny]==0:
                temp[nx][ny]=temp[x][y]+1
                q.append((nx,ny))
            elif island[nx][ny] and temp[nx][ny]!=cnt:
                a.append(temp[x][y]-cnt)
    return min(a)
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            s=[]
            q_=deque()
            q_.append((i,j))
            s.append((i,j))
            graph[i][j]=cnt
            island[i][j]=True
            while q_:
                x,y=q_.popleft()
                for m in range(4):
                    nx=x+dx[m]
                    ny=y+dy[m]
                    if nx<0 or nx>=n or ny<0 or ny>=n: #벽인 경우 continue
                        continue    
                    if graph[nx][ny]==1:
                        graph[nx][ny]=cnt
                        island[nx][ny]=True
                        q_.append((nx,ny))
                        s.append((nx,ny))
            q.append(s)
            cnt_stack.append(cnt)
            cnt+=1
k=0
flag=False
for i in range(n):
    for j in range(n):
        if graph[i][j]==cnt_stack[k]:
            temp=[g[:] for g in graph]
            ans.append(bfs(temp,q.popleft(),graph[i][j]))
            k+=1
            if k>=len(cnt_stack):
                flag=True
                break
    if flag:
        break
print(min(ans))
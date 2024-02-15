from itertools import combinations,permutations
from collections import deque
import sys 
dx=[0,0,-1,1]
dy=[1,-1,0,0]
INF=9876543210

input = sys.stdin.readline

def calDist(A,B):
    return abs(A[0]-B[0])+abs(A[1]-B[1])

def isConnect(now_XY):
    visited=[[0 for j in range(5)] for i in range(5)]
    temp=[[0 for j in range(5)] for i in range(5)]
    for x,y in now_XY:
        temp[x][y]=1
    visited[now_XY[0][0]][now_XY[0][1]]=1
    count=1
    q=deque([[now_XY[0][0],now_XY[0][1]]])
    while(q):
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0 and temp[nx][ny]==1:
                visited[nx][ny]=1
                q.append([nx,ny])
                count+=1
    if count==size:
        return True
    else:
        return False


graph = [input().rstrip() for _ in range(5)]
stars_XY=[]
for i in range(5):
    for j in range(5):
        if graph[i][j]=="*":
            stars_XY.append([i,j])
size=len(stars_XY)

comb=list(combinations([i for i in range(25)],size))
answer=INF
for number in comb:
    number_XY=[]
    for i in number:
        x=i//5 #x좌표
        y=i%5 #y좌표
        number_XY.append([x,y])

    # 연결여부확인
    if not isConnect(number_XY):
        continue

    # 거리확인
    result=INF
    per=list(permutations([i for i in range(size)],size))
    for p in per:
        temp=0
        for i in range(size):
            temp+=calDist(stars_XY[i],number_XY[p[i]])
        if temp<result:
            result=temp

    if result<answer:
        answer=result

print(answer)
import sys
from collections import deque

n,m = map(int,input().split())

lands = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    land[(x,y)] = lands_number
    lands_info.append((lands_number,x,y))
    lands[x][y]=2
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and lands[nx][ny]==1:
                lands[nx][ny]=2
                q.append((nx,ny))
                land[(nx,ny)] = lands_number
                lands_info.append((lands_number,nx,ny))
lands_info = []
lands_number = 0
land = dict()
for i in range(n):
    for j in range(m):
        if lands[i][j]==1:
            bfs(i,j)
            lands_number+=1
edges=[]
for land_number, x, y in lands_info:
    for i in range(4):
        dist = 0
        nx = x + dx[i]
        ny = y + dy[i]
        while True:
            if 0<=nx<n and 0<=ny<m:
                current_land_number = land.get((nx,ny))
                if current_land_number == land_number:
                    break
                if current_land_number == None:
                    dist+=1
                    nx += dx[i]
                    ny += dy[i]
                    continue
                if dist<2:
                    break
                edges.append((dist,land_number,current_land_number))
                break
            else:
                break
edges.sort(reverse=True)
parents = [i for i in range(land_number+1)]
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parents[y] = x
    else:
        parents[x] = y

count=0
result=0
while count!=land_number:
    try:
        w,a,b = edges.pop()
    except:
        print(-1)
        exit()
    if find(a) != find(b):
        union(a,b)
        result+=w
        count+=1
print(result)
    
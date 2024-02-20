import sys
from collections import deque

n,m = map(int,input().split())

lands = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

#다리 위치 정보 저장
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

#다리 위치 정보를 통해 다리 놓기
for land_number, x, y in lands_info:
    for i in range(4):
        dist = 0
        nx = x + dx[i]
        ny = y + dy[i]
        while True:
            if 0<=nx<n and 0<=ny<m:
                current_land_number = land.get((nx,ny))
                #같은 섬인 경우
                if current_land_number == land_number:
                    break
                #물 위에 있는 경우
                if current_land_number == None:
                    dist+=1
                    #같은 dx, dy 값을 더해주므로써 다리 놓는 방향 일관성 유지
                    nx += dx[i]
                    ny += dy[i]
                    continue
                #거리가 2보다 작은 경우 
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
#크루스칼 알고리즘 구현
while count!=land_number:
    #조건을 만족하는 섬이 없는 경우를 구분하기 위해 try, except 사용
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
    

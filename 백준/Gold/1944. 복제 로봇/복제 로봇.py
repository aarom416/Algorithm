import sys, heapq
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [input() for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
obj = dict()
dist = [[-1]*n for _ in range(n)]
edges = [[] for _ in range(m+1)]
obj_count=0
obj_loc = []

for i in range(n):
    for j in range(n):
        if graph[i][j]=='S' or graph[i][j]=='K':
            obj[(i,j)]=obj_count
            obj_count+=1
            obj_loc.append((i,j))
q = deque()
for x1,y1 in obj_loc:
    q.append((x1,y1))
    dist = [[-1]*n for _ in range(n)]
    dist[x1][y1]=0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!='1' and dist[nx][ny]==-1:
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
    for a,b in obj_loc:
        if dist[a][b]>0:
            edges[obj.get((x1,y1))].append((dist[a][b],obj.get((a,b))))
heap = [(0,0)]
result=0
count=0
edges_visited = [False]*(m+1)
while count!=m+1:
    try:
        dist,s = heapq.heappop(heap)
    except:
        print(-1)
        exit()
    if not edges_visited[s]:
        edges_visited[s]=True
        result+=dist
        count+=1     
        for i in edges[s]:
            heapq.heappush(heap,i)
print(result)
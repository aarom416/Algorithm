import sys, heapq
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [input() for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0] 
obj = dict() #로봇과 시작점을 나타낼 변수
dist = [[-1]*n for _ in range(n)]
edges = [[] for _ in range(m+1)]
obj_count=0
obj_loc = []

#각 객체의 정보(위치, 번호)를 저장
for i in range(n):
    for j in range(n):
        if graph[i][j]=='S' or graph[i][j]=='K':
            obj[(i,j)]=obj_count
            obj_count+=1
            obj_loc.append((i,j))
q = deque()
#BFS를 통해 각 정점에서 다른 정점까지의 거리 정보(다른 정점 번호까지 거리, 다른 정점 번호) 저장
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
    #거리 확인
    for a,b in obj_loc:
        if dist[a][b]>0:
            edges[obj.get((x1,y1))].append((dist[a][b],obj.get((a,b))))
heap = [(0,0)]
result=0
count=0
edges_visited = [False]*(m+1)
#프림 알고리즘을 사용하여 최단 거리 확인
while count!=m+1:
    #객체의 개수가 맞지 않아 비어있는 힙에서 pop하는 경우 try,except 부분으로 -1 처리
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

import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]
result = 0 
def bfs():
    global result #최종 감염되지 않는 값을 전역으로 관리하기 위해 global 변수 사용
    q = deque()
    temp_graph = copy.deepcopy(graph)
    for a in range(n): #감염된 영역이 전파되는 영역을 한번에 구하기 위해 큐에 먼저 다 넣음
        for b in range(m):
            if temp_graph[a][b] == 2:
                q.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if temp_graph[nx][ny]==0: #감염된 영역 전파
                temp_graph[nx][ny]=2
                q.append((nx,ny))
    count=0
    for p in range(n): #감염되지 않은 영역 확인
        for q in range(m):
            if temp_graph[p][q]==0:
                count+=1
    result = max(result, count) #최대값 갱신
    
def make_well(count): #벽 세우는 로직
    if count==3: #벽을 3번 세우면 bfs 
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                make_well(count+1) #재귀를 사용하여 count함
                graph[i][j]=0 # 원래대로 graph을 돌려줌

make_well(0)
print(result)
        

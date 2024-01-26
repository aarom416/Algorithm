import sys
import heapq

input = sys.stdin.readline

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
dp = [[0]*n for _ in range(m)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs():
    dp[0][0]=1
    q = [(-graph[0][0],0,0)] #높은 내리막길부터 탐색하기 위해 (우선순위 heapq 사용) - queue 사용하면 먼저 업데이트됨
    while q:    
        h,x,y = heapq.heappop(q)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[nx][ny]<graph[x][y]:
                if dp[nx][ny]==0:
                    heapq.heappush(q,(-graph[nx][ny],nx,ny))
                dp[nx][ny] = dp[nx][ny]+dp[x][y]
bfs()
print(dp[m-1][n-1])

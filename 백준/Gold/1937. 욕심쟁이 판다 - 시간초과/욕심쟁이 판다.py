#처음 풀이 - 시간초과 -> 처음엔 bfs 사용했는데 bfs는 깊게 보는게 아니라 넓게 모든 경우를 다 보기 때문에 시간초과가 떴던거 같다. 
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    dp = [[0]*n for _ in range(n)]
    max_result=0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]>graph[x][y]:
                dp[nx][ny]=dp[x][y]+1
                q.append([nx,ny])
                if max_result<dp[nx][ny]:
                    max_result=dp[nx][ny]
    return max_result
result=[]
for i in range(n):
    for j in range(n):
        result.append(bfs(i,j))
print(max(result)+1)

#다른 풀이 - dfs 사용해서 깊이 최대값을 확인하여 최대 방문할 수 있는 경우로 dp 값을 갱신하여 풀이
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
dp = [[0]*n for _ in range(n)]
result=0

def dfs(x,y):
    if dp[x][y]:
        return dp[x][y] #이미 방문한 곳은 그대로 리턴
    dp[x][y]=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]>graph[x][y]:
            dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

for i in range(n):
    for j in range(n):
        result = max(dfs(i,j),result)



print(result)

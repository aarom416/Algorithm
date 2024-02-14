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
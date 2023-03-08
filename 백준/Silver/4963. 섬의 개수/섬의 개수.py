#dfs 풀이
import sys
sys.setrecursionlimit(10**6) #파이썬은 재귀깊이가 1000으로 설정되있으므로 그 이상 재귀호출이 일어날 수 있게 설정해줌
input=sys.stdin.readline
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m: #밖으로 나가면 False
        return False
    if graph[x][y]==1: #1이면 dfs 재귀 진행
        graph[x][y]=0
        dfs(x-1,y-1)
        dfs(x-1,y)
        dfs(x-1,y+1)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y-1)
        dfs(x+1,y)
        dfs(x+1,y+1)
        return True
    return False
while True:
    m,n=map(int,input().split())
    if n==0 and m==0:
        break
    graph=[list(map(int,input().split())) for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt+=1
    print(cnt)
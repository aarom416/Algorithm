import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R,C = map(int,input().split())
graph = [list(input()) for _ in range(R)]

visited = [[False]*(C) for _ in range(R)]
count=0 
def dfs(x,y):
    global count,flag
    if flag:
        return
    if x<0 or x>=R or y<0 or y>=C or visited[x][y] or graph[x][y] == 'x':
        return
    visited[x][y]=True
    if y==C-1:
        count+=1
        flag = True
    dfs(x-1,y+1)
    dfs(x,y+1)
    dfs(x+1,y+1)
    
for i in range(R):
    flag = False
    dfs(i,0)
print(count)
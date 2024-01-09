import sys
sys.setrecursionlimit(10**6)
n=int(input())
max_height = 0
graph = []
result_list = [0]
for _ in range(n):
    g = list(map(int, input().split()))
    max_height = max(max(g),max_height)
    graph.append(g)

def dfs(x,y,height,v):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if not v[x][y] and graph[x][y] > height:
        v[x][y] = True
        dfs(x-1,y,height,v)
        dfs(x+1,y,height,v)
        dfs(x,y+1,height,v)
        dfs(x,y-1,height,v)
        return True
    return False

for h in range(0,max_height):
    visited = [[False]*n for _ in range(n)]
    result=0
    for i in range(n):
        for j in range(n):
            if dfs(i,j,h,visited):
                result+=1
    result_list.append(result)
   
print(max(result_list))
import sys
sys.setrecursionlimit(10**6) #재귀함수 1000000 번으로 제한
n=int(input())
max_height = 0
graph = []
result_list = []
# graph 와 최대 높이를 계산하는 로직
for _ in range(n): 
    g = list(map(int, input().split()))
    max_height = max(max(g),max_height)
    graph.append(g)

#dfs 로직
def dfs(x,y,height,v): 
    if x<0 or x>=n or y<0 or y>=n: #경로에 벗어난 경우
        return False
    if not v[x][y] and graph[x][y] > height: #방문하지 않고 비가 오는 높이보다 큰 경우
        v[x][y] = True
        dfs(x-1,y,height,v)
        dfs(x+1,y,height,v)
        dfs(x,y+1,height,v)
        dfs(x,y-1,height,v)
        return True
    return False

for h in range(0,max_height): #최대 높이 전까지 잠기지 않은 영역 확인 - 비가 오지 않는 경우도 포함
    visited = [[False]*n for _ in range(n)] #방문 영역 초기화
    result=0
    for i in range(n):
        for j in range(n):
            if dfs(i,j,h,visited):
                result+=1
    result_list.append(result)
   
print(max(result_list))

from collections import deque
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
dfs_visited=[False]*(n+1)
bfs_visited=[False]*(n+1)
dfs_stack=[]
bfs_stack=[]
def dfs(x):
    dfs_visited[x]=True
    dfs_stack.append(x)
    for i in graph[x]:
        if not dfs_visited[i]:
            dfs(i)
    return dfs_stack
def bfs(x):
    q=deque([x])
    bfs_visited[x]=True
    while q:
        v=q.popleft()
        bfs_stack.append(v)
        for i in graph[v]:
            if not bfs_visited[i]:
                bfs_visited[i]=True
                q.append(i)
    return bfs_stack
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort() #정점 번호가 작은 것부터 먼저 방문하기 위해 오름차순 정렬
    graph[b].sort() #정점 번호가 작은 것부터 먼저 방문하기 위해 오름차순 정렬
print(*dfs(v))
print(*bfs(v))

#다른 풀이 - 작은 숫자부터 탐색을 위해 2차원 리스트로 구현
from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
  q = deque()
  q.append(v)       
  visit_list[v] = 1   
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list[i] = 1

def dfs(v):
  visit_list2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)

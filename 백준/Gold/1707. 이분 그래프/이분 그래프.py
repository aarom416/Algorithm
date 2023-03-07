import sys
sys.setrecursionlimit(10**6) #파이썬은 재귀깊이가 1000으로 설정되있으므로 그 이상 재귀호출이 일어날 수 있게 설정해줌
input=sys.stdin.readline
def dfs(v,group):
    global error
    if error:
        return
    visited[v]=group #해당 그룹 설정
    for i in graph[v]:
        if not visited[i]:
            dfs(i,-group) #다른 그룹 설정 ex) 전 숫자가 -1 그룹이면 현재는 1 그룹
        elif visited[i]==visited[v]: #인접한 정점이 같은 그룹이면
            error=True
            return #재귀 리턴
k=int(input())
for _ in range(k):
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    visited=[False]*(n+1)
    error=False
    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i,1)
            if error:
                break
    if error:
        print('NO')
    else:
        print('YES')
    
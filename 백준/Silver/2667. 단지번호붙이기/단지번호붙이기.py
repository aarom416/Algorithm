from collections import deque
import sys
sys.setrecursionlimit(10**6) #파이썬은 재귀깊이가 1000으로 설정되있으므로 그 이상 재귀호출이 일어날 수 있게 설정해줌
input=sys.stdin.readline
def dfs(x,y):
    global cnt
    if x<0 or x>=n or y<0 or y>=n: #벽에 닿으면 리턴
        return
    if not visited[x][y] and graph[x][y]==1: 
        visited[x][y]=True
        cnt+=1
        dfs(x+1,y) #상하좌우 dfs 재귀
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
    
n=int(input())
graph=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
stack=[]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]==1: #방문하지 않고 1이면 dfs 진행
            cnt=0
            dfs(i,j) #dfs 모두 완료되면 전역변수 cnt을 stack에 넣음
            stack.append(cnt)
print(len(stack)) #stack의 개수 = 단지수
stack.sort() #오름차순 정렬
for i in stack:
    print(i)
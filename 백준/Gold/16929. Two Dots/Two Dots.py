n,m=map(int,input().split())
graph=[list(input()) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(color,x,y,cnt,start_x,start_y):
    for i in range(4): #동서남북 방향으로 dfs 수행
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n: #벽에 닿거나 나가면 continue
            continue
        if cnt>=4 and nx==start_x and ny==start_y: #색이 같고 시작점과 같으면 cycle 생성된 것
            print('Yes')
            exit()
        if not visited[ny][nx] and graph[ny][nx]==color: #색이 같고 방문하지 않으면
            visited[ny][nx]=True #방문 등록
            dfs(color,nx,ny,cnt+1,start_x,start_y) #이동한 좌표와 cnt+1을 갖고 dfs 수행
            visited[ny][nx]=False #방문 해제-> 해제해야 다음 점에서의 cycle 있는 지 확인 가능
for i in range(n):
    for j in range(m):
        start_x=j #시작점 저장
        start_y=i
        visited[i][j]=True
        dfs(graph[i][j],j,i,1,start_x,start_y)
print('No')
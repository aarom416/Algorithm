from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
island=[[False]*n for _ in range(n)] #섬을 파악하기 위한 2차원 리스트
cnt=2 #섬을 구분하기 위한 변수 cnt=2는 2번섬
cnt_stack=[] #섬 번호를 모아둘 리스트
q=deque() #각각의 섬 좌표 리스트들을 모아둘 데크
ans=[] #결과 리스트
#다른 섬과 거리를 구하기 위한 bfs
def bfs(temp,q,cnt):
    bridge_len=[] #현재 섬으로부터 다른 섬으로 다리를 지었을때 필요한 다리 길이를 모아둘 리스트
    q=deque(q) #현재 q는 리스트 형태이므로 q를 다시 데크 형태로 변환
    while q: 
        x,y=q.popleft() 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: #벽인 경우 continue
                continue
            if temp[nx][ny]==cnt: #인접한 좌표가 같은 섬인 경우
                continue
            if temp[nx][ny]==0: #인접한 좌표가 바다인 경우
                temp[nx][ny]=temp[x][y]+1 #다리 놓기
                q.append((nx,ny))
            elif island[nx][ny] and temp[nx][ny]!=cnt: #인접한 좌표가 섬이고 섬의 번호가 다른 경우-> 다른 섬인 경우
                bridge_len.append(temp[x][y]-cnt) #섬의 번호에서 증가했으므로 다리의 길이는 해당 값에서 섬의 번호를 빼야함
    return min(bridge_len) #필요한 다리 길이 중 가장 작은 값 리턴
#섬의 위치를 파악하고 구분하기 위한 bfs
for i in range(n): 
    for j in range(n):
        if graph[i][j]==1:
            s=[] #섬의 좌표를 튜플 형태로 한번에 모아두는 리스트
            q_=deque()
            q_.append((i,j)) 
            s.append((i,j))
            graph[i][j]=cnt #처음 cnt번 섬으로 구분
            island[i][j]=True #처음 섬으로 선언
            while q_:
                x,y=q_.popleft()
                for m in range(4):
                    nx=x+dx[m]
                    ny=y+dy[m]
                    if nx<0 or nx>=n or ny<0 or ny>=n: #벽인 경우 continue
                        continue    
                    if graph[nx][ny]==1: #인접한 섬인 경우
                        graph[nx][ny]=cnt #cnt번 섬으로 구분
                        island[nx][ny]=True #섬으로 선언
                        q_.append((nx,ny))
                        s.append((nx,ny)) #섬 좌표 계속 모아둠
            #인접한 섬에 대한 bfs가 모두 끝나면
            q.append(s) #계속 모아두었던 섬 좌표 리스트를 다른 bfs에 queue로 사용하기 위해 넣어둠 -> 섬 좌표 구분,파악이 모두 끝나면 2중 리스트 형태로 저장 되어있음
            cnt_stack.append(cnt) #몇 번 섬인지 체크
            cnt+=1
k=0 #현재 섬 체크를 몇 번 했는지에 대한 변수
flag=False #모든 섬을 체크했는지에 대한 변수
for i in range(n):
    for j in range(n):
        if graph[i][j]==cnt_stack[k]: #현재 섬이라면
            temp=[g[:] for g in graph] #각각의 섬에 대한 bfs를 수행해야함->graph를 slicing을 하여 깊은 복사 수행
            ans.append(bfs(temp,q.popleft(),graph[i][j])) #복사한 graph와,제일 앞에 있는 모아두었던 섬 좌표 리스트와, 현재 섬 번호를 인자로 bfs 수행
            k+=1
            if k>=len(cnt_stack): #섬 체크를 모두 완료하면
                flag=True #모든 섬 체크 완료 표시
                break
    if flag:
        break
print(min(ans)) #각각 섬에서 다른 섬으로까지 가장 짧은 다리의 길이들 중 가장 작은 값 출력

#시간 초과 - 불필요한 재귀 사용으로 인한 것으로 예상됨
from collections import deque
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n=int(input())
station=[[] for _ in range(n+1)] #역
visited=[False]*(n+1) 
cycle_list=[False]*(n+1) #순환선을 담는 리스트
check=[-1]*(n+1) #결과 리스트
def dfs(x,s,cnt): #dfs 사용해 순환선 찾기
    global cycle
    if cnt>=3 and x==s: # 다음 역이 처음 출발한 역과 같고 3개 이상의 역을 지났다면=순환선이면
        cycle=True #순환선 표시 후 리턴
        return
    visited[x]=True #방문처리
    for i in station[x]: # 다음 역들 중에서
        if not visited[i]: #순환선이 아니면 
            dfs(i,s,cnt+1) #다음 역 재귀 반복
        elif i==s and cnt>=3: #다음 역이 처음 출발한 역과 같고 3개 이상의 역을 지났다면
            dfs(i,s,cnt) #cnt를 증가하지 않고 재귀 수행
def bfs(): #bfs 사용해 순환선까지 거리 찾기(최단 거리)
    q=deque()
    for i in range(1,n+1):
        if cycle_list[i]: #순환역이면
            check[i]=0  #0으로 처리하여 순환선 구분(순환선 아닌 역은 -1)
            q.append(i)
    while q:
        x=q.popleft()
        for i in station[x]: #다음 역들 중에서
            if check[i]==-1: #순환선 아닌 역이면
                q.append(i)
                check[i]=check[x]+1 #현재 역의 값은 방금 전역 값+1 해야 순환선까지 거리 구해짐
    for i in range(1,n+1):
        print(check[i],end=' ')
    return
                    
for _ in range(n):
    a,b=map(int,input().split())
    station[a].append(b)
    station[b].append(a)
for i in range(1,n+1):
    start=i #처음 값 기억
    cycle=False #순환선인지 확인할 값
    visited=[False]*(n+1)
    dfs(i,start,1) 
    if cycle: #순환선이라면
        cycle_list[i]=True #해당 역이 순환선임을 표시
bfs()

#다른 풀이(참조)
from collections import deque
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
n=int(input())
station=[[] for _ in range(n+1)] #현재 역 설정을 위한 리스트
next_station=[0]*(n+1) #다음 역 설정을 위한 리스트(순환선이 아닌 역)->순환선이면 0으로 처리
temp=[[] for _ in range(n+1)] #다음 역 설정 처리를 위해 임의로 만든 리스트
station_size=[0]*(n+1) #각 역의 간선 수를 처리할 리스트
answer=[-1]*(n+1) #결과 리스트
def bfs(): #순환선으로부터 떨어진 거리 구하는 bfs
    q=deque()
    for i in range(1,n+1): #순환선인 역 찾기
        if next_station[i]==0: #순환선이면
            answer[i]=0 #결과 0
            q.append(i) 
    while q:
        x=q.popleft()
        for i in station[x]:
            if answer[i]==-1: #순환선이 아닌 역이면
                answer[i]=answer[x]+1 #현재 역의 전 역값의+1
                q.append(i)
for _ in range(n):
    a,b=map(int,input().split())
    station[a].append(b) #인접한 역 설정
    station[b].append(a)
    temp[a].append(b) #다음 역 처리를 위해 설정
    temp[b].append(a)
    station_size[a]+=1 #간선 수 설정
    station_size[b]+=1
while True:
    flag=True
    for i in range(1,n+1): #간선 수가 1개가 존재하지 않을때까지 반복->순환선만 존재하도록
        if station_size[i]==1: #간선 수가 1개라는것은 순환선 밖에 제일 마지막 역을 의미
            next=temp[i].pop() #다음 역 pop->temp리스트 사용 이유:bfs에서 station리스트 사용해야함
            next_station[i]=next #다음 역 리스트에 삽입
            temp[next].remove(i) #현재 역과 다음 역과 연결된 간선 삭제
            station_size[i]=0 #현재 역의 간선 0으로 변경
            station_size[next]-=1 #다음 역의 간선은 하나 줄으므로 -1
            flag=False #간선 수 다시 체크
    if flag: #간선 수 1개인 역이 없으면 순환선만 존재한다는 것으로 break-> 이때 순환선 역의 간선 수는 2개, 순환선이 아닌 역의 간선 수는 0개
        break 
bfs() # bfs 사용하여 순환선 아닌 역까지의 거리 구함
for i in range(1,n+1):
    print(answer[i],end=' ')

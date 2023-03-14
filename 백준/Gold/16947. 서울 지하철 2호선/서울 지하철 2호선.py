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
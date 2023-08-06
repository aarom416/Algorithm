import sys
import heapq
input=sys.stdin.readline
n=int(input())
time=[]
end_time=[]
for _ in range(n):
    a,b=map(int,input().split())
    time.append([a,b])
time.sort() #시작 시간으로 정렬
heapq.heappush(end_time,time[0][1])
#가장 먼저 끝나는 종료 시간을 우선으로 정렬을 유지하므로써 종료 시간에 따라 강의실을 추가할지 결정
for i in range(1,n):
    if time[i][0]<end_time[0]: #현재 종료 시간이 기록된 가장 먼저 끝나는 종료시간보다 작으면 강의실 추가를 위해 현재 종료 시간 추가
        heapq.heappush(end_time,time[i][1])
    else: #크면 강의실을 이어가면 되므로 종료 시간 제거 후 새로운 종료 시간 추가하여 자동으로 정렬 유지
        heapq.heappop(end_time)
        heapq.heappush(end_time,time[i][1])
print(len(end_time))
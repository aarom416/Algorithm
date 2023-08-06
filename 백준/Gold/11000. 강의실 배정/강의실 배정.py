import sys
import heapq
input=sys.stdin.readline
n=int(input())
time=[]
end_time=[]
for _ in range(n):
    a,b=map(int,input().split())
    time.append([a,b])
time.sort()
heapq.heappush(end_time,time[0][1])
for i in range(1,n):
    if time[i][0]<end_time[0]:
        heapq.heappush(end_time,time[i][1])
    else:
        heapq.heappop(end_time)
        heapq.heappush(end_time,time[i][1])
print(len(end_time))
import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())
INF = int(1e9)
computers = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
visited = [0] * (n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    computers[a].append((b,c))
    computers[b].append((a,c))
def dijkstra():
    heap = []
    heapq.heappush(heap,(0,1))
    dist[1]=0
    while heap:
        distance, now = heapq.heappop(heap)
        if dist[now] < distance:
            continue
        for i in computers[now]:
            cost = distance+i[1]
            if cost < dist[i[0]]:
                dist[i[0]]=cost
                visited[i[0]]=now
                heapq.heappush(heap,(cost,i[0]))
dijkstra()
count=0
connect = []
for i in range(2,len(dist)):
    if dist[i] != 1e9:
        count+=1
    if visited[i] != 0:
        connect.append((i,visited[i]))
print(count)
for a,b in connect:
    print(a,b)
import sys, heapq

input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())

dist = [INF] * (n+1)
citys = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    citys[a].append((b,cost))
start,end = map(int,input().split())
def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start))
    dist[start]=0
    while heap:
        distance, now = heapq.heappop(heap)
        if dist[now]<distance:
            continue
        for i in citys[now]:
            cost = distance+i[1]
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(heap,(cost,i[0]))
dijkstra(start)
print(dist[end])

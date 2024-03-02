import sys, heapq

input = sys.stdin.readline

n,m,start = map(int,input().split())

INF = int(1e9)

roads = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
#목적지에서 집으로 가는 거리를 저장하기 위한 다익스트라 알고리즘
def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start))
    dist[start] = 0
    while heap:
        distance, now = heapq.heappop(heap)
        if dist[now]<distance:
            continue
        for i in roads[now]:
            cost = distance+i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))

#집에서 목적지 가는 거리를 반환하는 다익스트라 알고리즘
def go(start,x):
    heap = []
    dist = [INF] * (n+1)
    heapq.heappush(heap,(0,start))
    dist[start] = 0
    while heap:
        distance, now = heapq.heappop(heap)
        if dist[now]<distance:
            continue
        for i in roads[now]:
            cost = distance+i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))
    return dist[x]
come_roads = [0] * (n+1)
for _ in range(m):
    a,b,x = map(int,input().split())
    roads[a].append((b,x))
#목적지에서 각 집으로 가는데 최단 거리 구해 저장
dijkstra(start)
#각 집에서 목적지까지 가는데 최단 거리 구해 저장
for i in range(1,n+1):
    come_roads[i] = go(i,start)
max_dist = 0
#목적지 갔다 오는 거리의 최대값 비교하며 갱신
for i in range(1,len(dist)):
    max_dist = max(max_dist, dist[i]+come_roads[i])
print(max_dist)

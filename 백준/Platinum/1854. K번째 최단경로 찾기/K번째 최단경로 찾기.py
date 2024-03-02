import sys, heapq

input = sys.stdin.readline

n,m,k = map(int,input().split())

INF = int(1e9)

roads = [[] for _ in range(n+1)]
#2차원 배열을 사용하여 k번쨰 수 확인
dist = [[INF]*(k) for _ in range(n+1)]
def dijkstra():
    heap = []
    heapq.heappush(heap,(0,1))
    dist[1][0] = 0
    while heap:
        distance, now = heapq.heappop(heap)
        if dist[now][k-1]<distance:
            continue
        for i in roads[now]:
            cost = distance+i[1]
            if cost < dist[i[0]][k-1]:
                dist[i[0]][k-1] = cost
                #오름차순 정렬
                dist[i[0]].sort()
                heapq.heappush(heap,(cost,i[0]))
for _ in range(m):
    a,b,x = map(int,input().split())
    roads[a].append((b,x))

dijkstra()

for i in range(1,n+1):
    if dist[i][k-1] == 1e9:
        print(-1)
    else:
        print(dist[i][k-1])
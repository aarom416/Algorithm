import sys, heapq

input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())

dist = [INF] * (n+1)
citys = [[] for _ in range(n+1)]
parents = [0] * (n+1)
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
                #현재 노드(now)를 해당 노드(i[0])의 부모 노드로 갱신
                parents[i[0]] = now
dijkstra(start)
visited = [end]
temp = end
#부모 노드를 찾아가면 경로 넣어줌 - 역추적
while temp!=start: 
    temp = parents[temp]
    visited.append(temp)
print(dist[end])
print(len(visited))
print(*visited[::-1])

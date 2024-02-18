import sys
import heapq 

input = sys.stdin.readline

n = int(input())
m = int(input())

heap = [[0,1]]
edge_list = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    start,end,weight = map(int,input().split())
    edge_list[start].append([weight,end])
    edge_list[end].append([weight,start])
    
result=0
while heap:
    w,s = heapq.heappop(heap)
    if not visited[s]:
        visited[s]=True
        result+=w
        for i in edge_list[s]:
            heapq.heappush(heap,i)
print(result)

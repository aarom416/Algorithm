import sys
import heapq 

input = sys.stdin.readline

v,e = map(int,input().split())
visited = [False]*(v+1)
heap = [[0,1]]
result=0
edge_list = [[] for _ in range(v+1)]

for _ in range(e):
    start, end, weight = map(int,input().split())
    edge_list[start].append([weight,end])
    edge_list[end].append([weight,start])
    
count=0    
while count!=v:
    w,s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        count+=1
        result+=w
        for i in edge_list[s]:
            heapq.heappush(heap,i)
print(result)
#크루스칼 알고리즘 풀이
import sys

input = sys.stdin.readline

v,e = map(int,input().split())

nodes = [list(map(int,input().split())) for _ in range(e)]

nodes.sort(key=lambda x:x[2])
parent = [i for i in range(v+1)]

result=0

def find(x):
    if x!=parent[x]: #연결되어 있는 부모 노드 찾기 
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y
        
for start, end, value in nodes:
    if find(start) != find(end): #연결되어 있지 않은 경우
        union(start,end) #합치기
        result+=value
print(result)

#프림 알고리즘 풀이
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
            heapq.heappush(heap,i) #힙을 사용하여 무게 작은 것부터 정렬->크루스칼의 sort 역할
print(result)

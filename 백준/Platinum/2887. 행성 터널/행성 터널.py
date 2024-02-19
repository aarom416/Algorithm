#프림 알고리즘 풀이 (처음 풀이)
import sys, heapq

input = sys.stdin.readline

n = int(input())

xList = []
yList = []
zList = []
#각 좌표에서 가장 인접한 행성부터 확인하기 위해 x,y,z 좌표로 리스트 처리
for i in range(n):
    x,y,z = map(int,input().split())
    xList.append((x,i))
    yList.append((y,i))
    zList.append((z,i))    
#가까운 행성 먼저 확인하기 위해 오름차순 정렬
xList.sort()
yList.sort()
zList.sort()

edges=[[] for _ in range(n)]
#각 x,y,z 마다 행성간 거리를 간선으로 표현
for curList in xList,yList,zList:
    for i in range(1,n):
        w1,a=curList[i-1]
        w2,b=curList[i]
        edges[a].append((abs(w1-w2),b))
        edges[b].append((abs(w1-w2),a))
heap = [(0,0)]
visited = [False]*n
count=0
result=0
#프림 알고리즘 구현
while count!=n:
    w,s= heapq.heappop(heap)
    if not visited[s]:
        visited[s]=True
        count+=1
        result+=w
        for i in edges[s]:
            heapq.heappush(heap,i)
print(result)

#크루스칼 알고리즘 (다른 풀이) - 프림 알고리즘보다 더 빨랐음 -> 모든 행성이 이어져 있다고 가정하고(fully connected graph) 정렬해놓는 방법을 생각하여 간선이 정점의 개수보다 많은
#fully connected graph 인 경우 간선의 개수는 e = v(v-1)/2 이므로 elog(e)인 크루스칼보다 elog(v) 인 프림 알고리즘을 사용했다.
#하지만 크루스칼이 더 빨랐는데 단순 log 안에서의 2를 나누는거라 큰 차이를 주긴 힘들고 heap 구조를 사용하는 원인 때문에 프림이 더 느린것으로 예상된다.
import sys

input = sys.stdin.readline

n = int(input())

xList = []
yList = []
zList = []
for i in range(n):
    x,y,z = map(int,input().split())
    xList.append((x,i))
    yList.append((y,i))
    zList.append((z,i))    
xList.sort()
yList.sort()
zList.sort()
edges=[]
for curList in xList,yList,zList:
    for i in range(1,n):
        w1,a=curList[i-1]
        w2,b=curList[i]
        edges.append((abs(w1-w2),a,b))
edges.sort(reverse=True)
parents = [i for i in range(n+1)]

def find(x):
    #부모 노드가 같아질 때까지
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    #부모 노드가 더 작은 값을 같도록 일관성 유지
    if x<y:
        parents[y]=x
    else:
        parents[x]=y

count=0
result=0
while count!=n-1:        
    w,a,b = edges.pop()
    #연결되어 있지 않은 경우
    if find(a) != find(b):
        union(a,b) # 연결
        count+=1
        result+=w
print(result)

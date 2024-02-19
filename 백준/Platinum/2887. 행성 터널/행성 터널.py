import sys, heapq, math

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
edges=[[] for _ in range(n)]
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
while count!=n:
    w,s= heapq.heappop(heap)
    if not visited[s]:
        visited[s]=True
        count+=1
        result+=w
        for i in edges[s]:
            heapq.heappush(heap,i)
print(result)
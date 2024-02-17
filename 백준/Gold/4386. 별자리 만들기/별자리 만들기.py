import sys, heapq, math

input = sys.stdin.readline

n = int(input())

stars_XY = [list(map(float, input().split())) for _ in range(n)]
node = [[] for _ in range(n)]
visited=[False]*(n)
for i in range(n-1):
    dist = 0
    for j in range(i+1,n):
        dist = math.sqrt((stars_XY[i][0]-stars_XY[j][0])**2+(stars_XY[i][1]-stars_XY[j][1])**2)
        node[i].append((dist,j))
        node[j].append((dist,i))
heap = [(0.0,0)]
result=0
count=0  
while n!=count:
    d,s = heapq.heappop(heap)
    if not visited[s]:
        visited[s]=True
        count+=1
        result+=d
        for i in node[s]:
            heapq.heappush(heap,i)
print(round(result,2))
        
import sys, heapq
input = sys.stdin.readline

# 인접 리스트 생성
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# 프림 알고리즘 진행
hq,cnt = [(0,1)],n
visit = [False]*(n+1)
maxDist,total = 0,0
while cnt:
    curDist,curNode = heapq.heappop(hq)
    if visit[curNode]:
        continue
    
    cnt -= 1
    visit[curNode] = True
    maxDist = max(maxDist,curDist)
    total += curDist
    for toNode, toDist in graph[curNode]:
        if not visit[toNode]:
            heapq.heappush(hq,(toDist,toNode))
print(total-maxDist)
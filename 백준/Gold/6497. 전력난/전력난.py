import sys, heapq

input = sys.stdin.readline

while True:
    m,n = map(int,input().split())
    edges = [[] for _ in range(m)]
    heap = []
    visited = [False]*m
    total_cost = 0
    count=0
    cost=0
    heap = [(0,0)]
    if m==0 and n==0:
        break
    for _ in range(n):
        a,b,w = map(int,input().split())
        edges[a].append((w,b))
        edges[b].append((w,a))
        total_cost+=w
    while count!=m:
        w,s = heapq.heappop(heap)
        if not visited[s]:
            count+=1
            cost+=w
            visited[s]=True
            for i in edges[s]:
                heapq.heappush(heap,i)
    print(total_cost-cost)

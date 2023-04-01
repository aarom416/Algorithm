import sys
import heapq
input=sys.stdin.readline
heap=[]
n=int(input().rstrip())
for _ in range(n):
    x=int(input().rstrip())
    if x == 0 and not heap:
        print(0)
    elif x==0:
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap,-x)
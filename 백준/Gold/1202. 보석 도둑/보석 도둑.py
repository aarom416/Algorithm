import sys
import heapq
input=sys.stdin.readline
n,k=map(int,input().split())
answer=0
jewel=[]
for _ in range(n):
    heapq.heappush(jewel,list(map(int,input().split()))) #최소힙을 사용해 각 가방에 넣을 수 있는 모든 보석 찾기
bags=[]
for _ in range(k):
    bags.append(int(input().rstrip()))
bags.sort()
tmp_jewel=[]
for bag in bags:
    while jewel and bag>=jewel[0][0]:
        heapq.heappush(tmp_jewel, -heapq.heappop(jewel)[1]) #최대힙을 사용해 각 가방에 넣을 수 있는 보석 중 가장 가치가 큰 보석 찾기
    if tmp_jewel:
        answer-=heapq.heappop(tmp_jewel)
    elif not jewel:
        break
print(answer)
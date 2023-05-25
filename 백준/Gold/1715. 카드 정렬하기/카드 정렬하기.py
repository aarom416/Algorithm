import sys
import heapq
input=sys.stdin.readline
n=int(input())
total_mix=0
card_list=[int(input().rstrip()) for _ in range(n)]
if len(card_list)==1:
    print(0) #카드 개수가 1개면 비교 횟수 0
    exit()
heapq.heapify(card_list) # 작은 숫자끼리 더하기 위해 힙 사용
while len(card_list)!=1:
    sum=heapq.heappop(card_list)+heapq.heappop(card_list)
    total_mix+=sum
    heapq.heappush(card_list,sum)
print(total_mix)
import sys
import heapq

input = sys.stdin.readline
n = int(input())
hq = []
max_day = 0
result = 0

#heapq 모듈을 사용하여 점수에 따른 최대 힙 정렬
for _ in range(n):
    d,w = map(int, input().split())
    heapq.heappush(hq, (-w,d))
    if max_day<d:
        max_day = d
        
homework_list = [0]*(max_day+1)

while hq:
    w,d = heapq.heappop(hq)
    w = -w
    #해당 날짜에서 밑으로 내려가며 넣을 수 있는 자리가 있는지 확인
    #해당 마감 날짜 넣어주어야 하는데 같은 마감 남짜가 있는 경우 그 전날에 배정시키는 과정
    for day in range(d,0,-1): 
        if not homework_list[day]:
            result+=w
            homework_list[day]=w
            break
print(result)
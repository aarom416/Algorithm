import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0]>=K:
        return answer
    while True:
        first_scoville=heapq.heappop(scoville)
        second_scoville=heapq.heappop(scoville)
        add_scoville=first_scoville+second_scoville*2
        heapq.heappush(scoville,add_scoville)
        answer+=1
        if scoville[0]>=K:
            break
        if len(scoville)==1:
            answer=-1
            break
    return answer
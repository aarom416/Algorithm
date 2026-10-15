import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    count = 0
    
    while scoville[0] < K and len(scoville) > 1:
        
        new_scoville = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        
        heapq.heappush(scoville, new_scoville)
        
        count += 1
           
    if scoville[0] < K:
        return -1
    return count
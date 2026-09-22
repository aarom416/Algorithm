import heapq

def solution(scoville, K):

    heapq.heapify(scoville)
    
    count = 0
    while scoville:
        
        if scoville[0] >= K:
            break
            
        if len(scoville) < 2:
            count = -1
            break
            
        #제일 안매운
        n = heapq.heappop(scoville)
        #두번쨰로 안매운
        m = heapq.heappop(scoville)
        
        mix_scoville = n + (m*2)
        
        heapq.heappush(scoville, mix_scoville)
        
        count +=1
        
        if scoville[0] >= K:
            break
    
    return count
    
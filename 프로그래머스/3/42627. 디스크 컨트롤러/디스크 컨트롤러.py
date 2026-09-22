import heapq as hq

def solution(jobs):
    
    total_jobs_count = len(jobs)
    jobs.sort(key=lambda x:x[0], reverse=True)
    waiting_heap = []
    current_time = 0
    start_time = 0
    end_time = 0
    processing_time = 0
    request_time = 0
    response_list = []
    is_processing = False
    while jobs or waiting_heap or is_processing:
        
        # 대기 큐에 넣기 -> 소요시간 먼저 우선순위
        while jobs and current_time == jobs[-1][0]:
            r, p = jobs.pop()
            hq.heappush(waiting_heap, [p,r])
            
        # 작업 완료
        if is_processing and (current_time-start_time == processing_time):
            end_time = current_time
            is_processing = False
            response_list.append(end_time - request_time)
            
        # 작업 시작
        if not is_processing and waiting_heap:
            p,r = hq.heappop(waiting_heap)
            processing_time = p
            request_time = r
            start_time = current_time
            is_processing = True
            
        
        current_time += 1
        
    return sum(response_list)//total_jobs_count
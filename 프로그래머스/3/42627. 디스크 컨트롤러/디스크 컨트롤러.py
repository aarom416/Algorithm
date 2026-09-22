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

# 다른 풀이
import heapq as hq

def solution(jobs):
    total_jobs = len(jobs)
    
    # 1. tasks: 요청 시각(x[0])이 빠른 순으로 pop()하기 위해 reverse=True 정렬
    # (소요시간, 요청시각) 형태로 저장
    tasks = sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0]), reverse=True)
    
    q = []
    # 2. q (Min-Heap): (소요시간 p, 요청시각 r) 기준 최소 힙
    hq.heappush(q, tasks.pop())
    current_time, total_response_time = 0, 0
    
    while q:
        p, r = hq.heappop(q)
        # 3. max 사용: 하드디스크가 쉬었으면 (r + p), 연속 실행이면 (current_time + p)로 시간 점프
        current_time = max(p + r, current_time + p)
        total_response_time += current_time - r
        
        # 4. 현재 완료 시점(current_time) 이하로 들어온 요청들을 대기 큐(q)로 이동
        while tasks and tasks[-1][1] <= current_time:
            hq.heappush(q, tasks.pop())
            
        # 5. 대기 큐가 비어있고 남은 작업이 있다면 다음 가장 빠른 요청을 대기 큐에 투입 (Idle 공백기 처리)
        if tasks and not q:
            hq.heappush(q, tasks.pop())
            
    return total_response_time // total_jobs

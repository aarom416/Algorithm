from collections import deque
import heapq as hq

def solution(jobs):
    
    total_jobs = len(jobs)
    tasks = sorted([(x[1], x[0]) for x in jobs], key = lambda x: (x[1], x[0]), reverse = True)
    
    q = []
    hq.heappush(q, tasks.pop())
    current_time, total_response_time = 0,0
    
    while q:
        p, r = hq.heappop(q)
        current_time = max(p+r, current_time+p)
        total_response_time += current_time-r
        while tasks and tasks[-1][1] <= current_time:
            hq.heappush(q, tasks.pop())
        if tasks and not q:
            hq.heappush(q, tasks.pop())
    return total_response_time // total_jobs
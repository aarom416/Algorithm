from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    # 좌표가 아닌 컴퓨터 번호를 넣어 해당 번호와 연결되어 있는 번호를 탐색
    for i in range(n):
        if visited[i]:
            continue
        answer += 1
        queue = deque([i])
        visited[i] = True
        while queue:
            link = queue.popleft()
            
            for i in range(n):
                if computers[link][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
    return answer
        
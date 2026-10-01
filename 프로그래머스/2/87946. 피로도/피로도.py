def solution(k, dungeons):
    answer = 0
    
    visited = [False] * len(dungeons)
    
    def dfs(k, count):
        
        nonlocal answer
        
        answer = max(count, answer)
        
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k-dungeons[i][1], count + 1)
                # 백트래킹 (방문했던 건 dfs 이후 전 상태로 복구)
                # 어떤 던전을 먼저 가느냐에 따라 최종적으로 갈 수 있는 던전 개수가 달라지기 때문
                visited[i] = False
    
    dfs(k, 0)
    
    return answer



def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2]) #최소 비용 연결을 위해 오름차순 정렬
    connect = set([costs[0][0]]) #섬 사이에 연결을 확인할 집합
    
    #kruskal 알고리즘을 이용
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect: #섬이 서로 연결되어 있는 경우 continue
                continue
            if cost[0] in connect or cost[1] in connect: #섬 하나를 연결해야 하는 경우 
                answer+=cost[2]
                connect.update([cost[0], cost[1]])
                break
            
    return answer

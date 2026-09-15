from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    bridge_queue = deque(0 for _ in range(bridge_length))
    bridge_weight = 0
    truck_queue = deque(truck_weights)
    
    answer = 0
    while bridge_queue:
        
        answer += 1
        bridge_weight -= bridge_queue.popleft()
        
        if truck_queue:
            if bridge_weight + truck_queue[0] > weight:
                bridge_queue.append(0)
            else:
                current_truck_weight = truck_queue.popleft()
                bridge_weight += current_truck_weight
                bridge_queue.append(current_truck_weight)
            
    
    return answer
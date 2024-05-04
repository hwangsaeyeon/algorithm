from collections import deque 
def solution(bridge_length, weight, truck_weights):
    time = 0 
    q = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    
    idx = 0 
    sumi = 0 
    while len(truck_weights) > 0 : 
        time += 1 
        sumi = sumi - q.popleft()
    
        if sumi + truck_weights[0] <= weight : 
            q.append(truck_weights[0])
            sumi += truck_weights.popleft()
        else : 
            q.append(0)

        
        if sumi == 0 : 
            return time 
        
    return time + bridge_length
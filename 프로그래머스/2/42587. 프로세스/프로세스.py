from collections import deque
def solution(priorities, location):
    answer = 0
    
    priorities = deque(priorities)
    max_val = max(priorities)
    length = len(priorities)
    
    loc = deque([i for i in range(len(priorities))])
    
    

    while True : 
        pop = priorities.popleft()
        idx = loc.popleft() 
        
        
        if pop == max_val :         
            answer += 1
            
            if idx == location : 
                return answer 
                break 
            
            max_val = max(priorities)
            
        else :
            priorities.append(pop)
            loc.append(idx)
        
        
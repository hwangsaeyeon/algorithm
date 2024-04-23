import heapq 

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True : 
        
        small1 = heapq.heappop(scoville)
        if small1 >= K : break 
        answer += 1 
        small2 = heapq.heappop(scoville)
        mix = small1 + (small2 * 2)
        if len(scoville) == 0 :
            if mix < K : 
                answer = -1 
                break 
        
        heapq.heappush(scoville, mix)
        
       
    
    
    return answer
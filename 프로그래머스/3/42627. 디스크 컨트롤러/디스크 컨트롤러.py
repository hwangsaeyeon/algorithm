import heapq 
def solution(jobs):
    answer, now, cnt = 0,0,0
    start = -1 
    heap = []
    
    while cnt < len(jobs) : 
        for j in jobs : 
            request, length = j 
            if start < request <= now : 
                heapq.heappush(heap, [length, request])
            
        if len(heap) > 0 : 
            current = heapq.heappop(heap)
            start = now 
            now += current[0] #현재 시간 
            answer += (now - current[1]) #총 소요시간 
            cnt += 1 
        else : 
            now += 1 #현재 시간
    return int(answer / len(jobs))
import heapq 
def solution(operations):
    minlist = []
    
    for val in operations: 
        operation = val.split()

        if operation[0] == "I":
            heapq.heappush(minlist, int(operation[1]))
        
        if operation[0] == "D":
            if len(minlist) > 0 : #빈큐에서 삭제하라는 경우 해당 연산 무시 
                if int(operation[1]) == 1 : #최댓값 삭제 
                    minlist.sort(reverse=True)
                    minlist.remove(minlist[0])
                    heapq.heapify(minlist)
                
                else : #최솟값 삭제 
                    heapq.heappop(minlist)
    
    if len(minlist) == 0 : 
        return [0,0]
    elif len(minlist) == 1 : 
        return [minlist[0], minlist[0]]
    else : 
        return [max(minlist),heapq.heappop(minlist)]

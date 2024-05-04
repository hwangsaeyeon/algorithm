def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)) : 
        if (i+1) > citations[i] : 
            return i
        elif (i+1) == citations[i] : 
            return i+1 
    
    return len(citations)
            
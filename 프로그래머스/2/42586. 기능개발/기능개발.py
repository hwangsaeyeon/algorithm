def solution(progresses, speeds):
    answer = []
    stack = []
    
    for i in range(len(progresses)) : 
        if (100-progresses[i]) % speeds[i] != 0 : 
            day = (100 - progresses[i]) // speeds[i] + 1
        else : 
            day = (100 - progresses[i]) // speeds[i]
        stack.append(day)

    check, num = stack[0], 0
    
    for i in range(len(stack)) : 
        if stack[i] > check : 
            answer.append(num)
            check, num = stack[i], 1
        
        else : 
            num += 1 

        
    answer.append(num)
            
        
    
    return answer